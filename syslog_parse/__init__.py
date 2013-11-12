import syslog_parse.parse
import syslog_parse.gen
from syslog_parse.daemon import app


def do_parse():
  syslog_parse.parse.main()

def generate():
  syslog_parse.gen.main()

def run_daemon():
  app.run()
