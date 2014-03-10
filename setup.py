#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name             = 'syslog_parse',
    version          = '1.0.0',
    url              = 'https://github.com/SoftlySplinter/syslog-monitor',

    description      = 'Monitor syslog',

    # Package
    
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    entry_points={
        'console_scripts': [
            'syslog-parse = syslog_parse:do_parse',
            'syslog-gen = syslog_parse:generate',
            'syslog-restd = syslog_parse:run_daemon'
        ]
    },

    # Requirements

    install_requires=[
        'flask',
        'gunicorn',
        'statsd',
    ],
)
