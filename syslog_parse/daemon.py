import json
from threading import Thread
from flask import Flask, request

from syslog_parse.watcher import LogWatcher

class Daemon(Thread):
  def __init__(self):
    super(Daemon, self).__init__()
    self.logs = []
    self.processes = []

  def start(self):
    self.running = True
    super(Daemon, self).start()

  def run(self):
    while self.running:
      for watcher in self.logs:
        try:
          watcher.do_parse(self.do_statsd)
        except Exception:
          print "error"

  def do_statsd(self, process, sev):
    print "{0} - {1}".format(process, sev)

  def stop(self):
    print "Stopping..."
    self.running = False

  def add_log(self, log):
    self.logs.append(LogWatcher(log, self.processes))

  def del_log(self, log):
    self.logs.remove(log)

  def add_ps(self, ps):
    self.logs.append(ps)

  def del_ps(self, ps):
    self.processes.remove(log)

app = Flask(__name__)
daemon = Daemon()
  
@app.route("/", methods=["POST"])
def post_run():
  logfile = request.values["logfile"]
  try:
    return SyslogParser(logfile).parse()
  except IOError as e:
    return (json.dumps({"fileerror": str(e)}), 400)

@app.route("/start", methods=["POST"])
def start_daemon():
  daemon.start()
  return ("SysWatch started", 200)

@app.route("/stop", methods=["POST"])
def stop_daemon():
  daemon.stop()
  return ("SysWatch stopped", 200)

@app.route("/log", methods=["POST"])
def add_log():
  logfile = request.values["logfile"]
  daemon.add_log(logfile)
  return ("added", 200)

@app.route("/log/<id>", methods=["DELETE"])
def del_log():
  if "logfile" not in requests.values:
    return (json.dumps({"error": "No logfile specified"}), 400)
  logfile = request.values["logfile"]
  daemon.del_log(logfile)
  return ("", 200)
