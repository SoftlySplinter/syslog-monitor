import re
import json


class SyslogParser:
  syslogmap = {0: "Emergency", 1: "Alert", 2: "Critical", 3: "Error", 4: "Warning", 5: "Notice", 6: "Informational", 7: "Debug"}

  def __init__(self, filename):
    self.filename = filename

  def parse(self):
    """Analyses a logfile and counts the number of each severity exists.
       This information is then put into JSON format."""
    # format: <sf> timestamp machine prog: msg
    res = {i:0 for i in self.syslogmap.itervalues()}
    with open(self.filename) as file:
      for line in file:
        # regex to match the standard syslog format. Will group the priority.
        matches = re.match(r"\<(\d\d?\d?)\>\s*...\s+\d\d?\s+\d\d:\d\d:\d\d\s+.+\s+.+:\s+.+", line)
        if(matches == None):
          import sys
          sys.stderr.write("Not a syslog format\n")
        else:
          # Priority = facility * 8 + severity
          pri = int(matches.group(1))
          sev = pri % 8
          res[SyslogParser.syslogmap[sev]] += 1
    return json.dumps(res, indent=2)

def main():
  import sys
  print SyslogParser(sys.argv[1]).parse()

if __name__ == "__main__":
  main()
