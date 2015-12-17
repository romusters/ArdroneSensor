import getpass
import sys
import telnetlib

import time
import basebehavior.behaviorimplementation

import os


tn = telnetlib.Telnet("192.168.1.1")
print "connected"
tn.write("cat /dev/ttyPA0\n")

def is_number(s):
    try:
	if s == "":
		return False
        float(s)
        return True
    except ValueError:
        return False

while True:
    if 1:
	    n = 0
	    while True:
		    #if is_number(tn.read_until('\n')):
                print tn.read_until('\n')
         



