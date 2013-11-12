import re
import json

class SyslogParser:
  def __init__(self, filename):
    self.filename = filename
    self.syslogmap = {0: "Emergency", 1: "Alert", 2: "Critical", 3: "Error", 
                      4: "Warning", 5: "Notice", 6: "Informational", 7: "Debug"}

  def parse(self):
    # format: <sf> timestamp machine prog: msg
    res = {i:0 for i in self.syslogmap.itervalues()}
    with open(self.filename) as file:
      for line in file:
        # regex to match the standard syslog format. Will match the priority.
        matches = re.match(r"\<(\d\d?\d?)\>\s*...\s+\d\d?\s+\d\d:\d\d:\d\d\s+.+\s+.+:\s+.+", line)
        if(matches == None):
          print "Not a syslog format"
        else:
          pri = int(matches.group(1))
          sev = pri % 8
          # Uncomment the line below for details on facilities.
          # fac = pri - sev / 8
          res[self.syslogmap[sev]] += 1
    print json.dumps(res, indent=2)

if __name__ == "__main__":
  import sys
  SyslogParser(sys.argv[1]).parse()
