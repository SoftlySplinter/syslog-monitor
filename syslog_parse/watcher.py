import re
from datetime import datetime

class LogWatcher(object):
  def __init__(self, log, processes):
    print "Watching log {}".format(log)
    self.log = log
    self.pos = 0
    self.processes = processes
    self.do_parse(self.no_op)

  def no_op(self, sev, process):
    pass

  def do_parse(self, statsd_callback):
    """Analyses a logfile and counts the number of each severity exists.
       This information is then put into JSON format."""
    # format: <sf> timestamp machine prog: msg
    with open(self.log, "r+") as file:
      file.seek(self.pos)
      for line in file:
        # regex to match the standard syslog format. Will group the priority.
        matches = re.match(r"\<(\d\d?\d?)\>\s*(...\s+\d\d?\s+\d\d:\d\d:\d\d)\s+(.+)\s+(.+):\s+(.+)", line)
        if(matches == None):
          import sys
          sys.stderr.write("Not a syslog format\n")
        else:
          #log_time = datetime.strptime(matches.group(2), "%b %d %H:%M:%S")
          # Priority = facility * 8 + severity
          pri = int(matches.group(1))
          sev = pri % 8
          statsd_callback(matches.group(4), sev)
      self.pos = file.tell()

  def set_processes(self, processes):
    self.processes = processes
