#!/usr/bin/env python
import thread, time

def counter(myId, count):
    for i in range(count): 
        mutex.acquire()
        print 'thread number %d reporting in at %d...' % (myId, time.clock())
        time.sleep(1)
        mutex.release()

print time.clock()
mutex = thread.allocate_lock()
for i in range(5):
    thread.start_new(counter, (i, 3))

time.sleep(20) 
print 'Main thread exiting.'

