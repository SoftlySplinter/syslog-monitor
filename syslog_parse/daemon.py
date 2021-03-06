import json
from threading import Thread
from flask import Flask, request
import statsd

from syslog_parse.watcher import LogWatcher

class Daemon(Thread):
  def __init__(self, logs, ps):
    super(Daemon, self).__init__()
    self.logs = logs
    self.processes = ps
    self.running = False
    self.statsd = statsd.StatsClient('graphite.qa', 8123)

  def start(self):
    if self.running:
      return False
    self.running = True
    try:
      super(Daemon, self).start()
    except Exception as e:
      print e
    return True

  def run(self):
    while self.running:
      for watcher in self.logs:
        try:
          watcher.do_parse(self.do_statsd)
        except Exception as e:
          print e

  def do_statsd(self, process, sev):
    if process in self.processes:
      self.statsd.incr("syslogmonitor.{0}.{1}".format(process, sev))
      print "{0} - {1}".format(process, sev)
    else:
      print "{0} - {1} not logged".format(process, sev)


  def stop(self):
    if not self.running:
      return False
    self.running = False
    return True

  def add_log(self, log):
    self.logs.append(LogWatcher(log, self.processes))

  def del_log(self, log):
    self.logs.remove(log)

  def add_ps(self, ps):
    self.processes.append(ps)
    for watcher in self.logs:
      watcher.set_processes(self.processes)

  def del_ps(self, ps):
    self.processes.remove(ps)
    for watcher in self.logs:
      watcher.set_processes(self.processes)

app = Flask(__name__)
daemon = Daemon([], [])

@app.route("/", methods=["POST"])
def post_run():
  logfile = request.values["logfile"]
  try:
    return SyslogParser(logfile).parse()
  except IOError as e:
    return (json.dumps({"fileerror": str(e)}), 400)

@app.route("/start", methods=["POST"])
def start_daemon():
  if daemon.isAlive():
    return ("SysWatch already started", 400)

  if daemon.start():
    return ("SysWatch started", 200)
  else:
    return ("SysWatch already started", 400)

@app.route("/stop", methods=["POST"])
def stop_daemon():
  if daemon.stop():
    return ("SysWatch stopped", 200)
  else:
    return ("SysWatch not started", 400)

@app.route("/log", methods=["POST"])
def add_log():
  logfile = request.values["logfile"]
  daemon.add_log(logfile)
  return ("", 200)

@app.route("/log/<id>", methods=["DELETE"])
def del_log(id):
  daemon.del_log(id)
  return ("", 200)

@app.route("/ps", methods=["POST"])
def add_ps():
  process = request.values["process"]
  daemon.add_ps(process)
  return ("", 200)

@app.route("/ps/<id>", methods=["DELETE"])
def del_ps(id):
  daemon.del_ps(id)
  return ("", 200)

