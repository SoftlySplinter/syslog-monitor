import json
from flask import Flask, request

from syslog_parse.parse import SyslogParser



app = Flask(__name__)
  
@app.route("/", methods=["POST"])
def post_run():
  logfile = request.values["logfile"]
  try:
    return SyslogParser(logfile).parse()
  except IOError as e:
    return (json.dumps({"error": str(e)}), 400)
