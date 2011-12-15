#!/usr/bin/env python

"""A fork that demonstrates a copied environment"""

import os
from os import environ

def my_fork():
    environ['FOO']="baz"
    print "FOO environmental variable set to: %s" % environ['FOO']
    environ['FOO']="bar"
    print "FOO environmental variable changed to: %s" % environ['FOO']
    child_pid = os.fork()
    if child_pid == 0:
        print "Child Process: PID# %s" % os.getpid()
        print "Child FOO environmental variable == %s" % environ['FOO']
    else:
        print "Parent Process: PID# %s" % os.getpid()
        print "Parent FOO environmental variable == %s" % environ['FOO']

if __name__ == "__main__":
    my_fork()

