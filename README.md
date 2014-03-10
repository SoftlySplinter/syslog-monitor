syslog-monitor
==============

Python syslog Monitor for DataSift Graduate Application

Dependencies
============

* Python
* Python setuptools
* Flask
* Python statsd

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


Dependencies
============

This tool requires python with the following libraries:

* python-setuptools
* flask (through setuptools)
* gunicorn (through setuptools)

