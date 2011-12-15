#!/usr/bin/env python

import os
import signal
import subprocess
import time

proc = subprocess.Popen('./sigchild.py')
print 'PARENT: Pausing before sending signal...'
time.sleep(1)
print 'PARENT: Signaling %s' % proc.pid
os.kill(proc.pid, signal.SIGUSR1)
