#!/usr/bin/env python

import os
import signal
import time

def signal_usr1(signum, frame):
   "Callback invoked when a signal is received"
   pid = os.getpid()
   print 'Received USR1 in process %s' % pid

print 'CHILD: Setting up signal handler'
signal.signal(signal.SIGUSR1, signal_usr1)
print 'CHILD: Pausing to wait for signal'
time.sleep(5)
