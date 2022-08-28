#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
# -------------------------------------------------------------------
# Created Date: Thursday, August 12th 2021, 10:23:38 am
# Author: Lc-Liu
# Contact: liu.lc.ch@gmail.com
# -----
# Copyright (c) 2021 Lc-Liu
# Apache License 2.0
# -------------------------------------------------------------------
'''


# https://stackoverflow.com/questions/57713184/how-to-write-logging-messages-to-a-file

import os, sys
import logging
import datetime as dt
import time

# Creación del archivo Log
LOG_FILE = os.getcwd() + "/logs"
if not os.path.exists(LOG_FILE):
    os.makedirs(LOG_FILE)
LOG_FILE = LOG_FILE + "/log.log"
logFormatter = logging.Formatter("%(levelname)s %(asctime)s %(message)s")
fileHandler = logging.FileHandler("{0}".format(LOG_FILE))
fileHandler.setFormatter(logFormatter)
stdout_handler = logging.StreamHandler(sys.stdout)
rootLogger = logging.getLogger()
rootLogger.addHandler(fileHandler)
rootLogger.addHandler(stdout_handler)
rootLogger.setLevel(logging.INFO)

time.sleep(3)
logging.info("Waited 3 seconds.")
time.sleep(3)

logging.info("testing out the logging functionality")
logging.error('error')
logging.critical('critic')
logging.warning('WARNING!\n')

try:
    print(10/0)
except Exception as e:
    logging.exception('Error ocurred.')