#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
# Created Date: Friday, May 14th 2021, 11:39:18 am
# Author: Lc-Liu
# Contact: liu.lc.ch@gmail.com
# -----
# Copyright (c) 2021 Lc-Liu
# Apache License 2.0
# -------------------------------------------------------------------
'''


from multiprocessing import Process
import time

def f(name):
    print('Starting thread:', name)
    time.sleep(25)
    print('Ending thread:', name)

class item:
    def f_kwargs(self, name='f_kwargs', id=0, type=None):
        print('Starting thread: ', name)
        print('Arg id:', id, '\tArg type:', type)
        time.sleep(25)
        print('Ending thread:', name)

if __name__=='__main__':
    i = item()
    p = Process(target=i.f_kwargs, kwargs={'id':2, 'type':'function'})
    print('Starting process.')
    p.start()
    print('Started process 1.')
    ## join waits for the process to stop.
    time.sleep(2)
    p.terminate()
    print('Ended process.')