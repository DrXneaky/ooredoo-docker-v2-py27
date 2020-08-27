#!/bin/bash

python cronjob_test.py | tee /var/log/cronlogs/cron60.log | msmtp ahess190@gmail.com

if grep -Fq "Error" /var/log/cronlogs/cron60.log 
	then 
		echo "`date` Error" | tee -a /var/log/cronlogs/cron60-history.log
	else
		echo "`date` Success" | tee -a /var/log/cronlogs/cron60-history.log
fi
