#!/bin/bash

grep 'ERROR' syslog.log | cut -d ' ' -f 6-150 > errorlog
sort -k 2 errorlog > errorlog_new
mv errorlog_new errorlog.out
rm errorlog
