syslog-monitor
==============

Python syslog Monitor for DataSift Graduate Application


Running
=======

To run the tool to produce syslog entires randomly run:

```sh
python syslog_test/__init__.py [lines] file
```

The file will default to `gen.log` if no file is specified.


To run the tool to parse the syslog file, run:

```sh
python syslog_parse/__init__.py file
```

This will return the results in JSON format to stdout.

Dependencies
============

All tools use Python 2.7.3 and libraries which come as standard.
