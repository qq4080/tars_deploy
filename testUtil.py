#!/usr/bin/python
# encoding: utf-8
import os
import comm.tarsUtil as tarsUtil
import comm.tarsLog as tarsLog
import subprocess
import sys
import time
import random
import re

log = tarsLog.getLogger()
def getAbabsolutePath():
    path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    return path

def cpTest():
    tarsUtil.copytree("/data/Tars/cpp/build/framework/deploy/tarsregistry","/usr/local/app/tars/")
    return

def startTest():
    return
def cmdTest():
    rCode = doCmd("/data/Tars/tars_deploy/pout.sh")
    if rCode == 0:
        print "ok"
    else :
        print "error"
    return

def doCmd(cmd):
    rCode=0
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline()
        line = line.strip()
        if line:
            log.info(line)
    if p.returncode == 0:
        rCode =0
    else:
        rCode=-1
    p.stdin.close()
    p.stdout.close()
    return rCode


if __name__ == '__main__':
    startTest()
    pass

