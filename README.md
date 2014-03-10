syslog-monitor
==============

Python syslog Monitor for DataSift Graduate Application

Dependencies
============

* Python
* Python setuptools
* Flask
* Python statsd
* Gunicorn

Installing
==========

To install using setuptools (pip/easy\_install) run:

```sh
python ./setup.py install
```


Running
=======

To run the log file generator run `syslog-gen [lines] file`.

To run the log file analyser run `syslog-parse file`.

To run the daemon run `./syslog-analyserd start`.

To stop the daemon run `./syslog-analyserd stop`.



API
===

Start
-----

To start the monitoring use:

`HTTP POST /start`


Stop
----

To stop the monitoring use:

`HTTP POST /stop`


Add Log
-------

To add a log file to monitor use:

```http
HTTP POST /log
log=<path/to/logfile>
```

Remove log
----------

Currently can't delete log files as their ID acts as a URL.

Would be done through

```http
HTTP DELETE /log/<logfile id>
```

Add process
-----------

```http
HTTP POST /ps
process=<name>
```

Remove process
--------------

```http
HTTP DELETE /ps/<ps id>
```
Dependencies
============

This tool requires python with the following libraries:

* python-setuptools
* flask (through setuptools)
* gunicorn (through setuptools)

