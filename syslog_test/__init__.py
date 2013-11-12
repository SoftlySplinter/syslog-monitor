import random
import time

def syslogtime():
  return time.strftime("%b  %d %H:%M:%S", time.gmtime())

for i in xrange(100):
  fac = random.randint(0,23)
  sev = random.randint(0,7)
  pri = fac * 8 + sev
  print "<{}>{} localhost syslog_test: Log message from fac: {}, sev:{}".format(pri, syslogtime(), fac, sev)
