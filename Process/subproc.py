#!/usr/bin/env python

import subprocess

# Simple command
subprocess.call('ls -l', shell=True)

# Command with shell expansion
subprocess.call('ls -l $HOME', shell=True)

print '\nread:'
proc = subprocess.Popen('echo "to stdout"',
                       shell=True,
                       stdout=subprocess.PIPE,
                       )
stdout_value = proc.communicate()[0]
print '\tstdout:', repr(stdout_value)


#Writing to the input of a pipe

print '\nwrite:'
proc = subprocess.Popen('cat -',
                       shell=True,
                       stdin=subprocess.PIPE,
                       )
proc.communicate('\tstdin: to stdin\n')

#Reading and writing

print '\npopen2:'

proc = subprocess.Popen('cat -',
                       shell=True,
                       stdin=subprocess.PIPE,
                       stdout=subprocess.PIPE,
                       )
stdout_value = proc.communicate('through stdin to stdout')[0]
print '\tpass through:', repr(stdout_value)

#Separate streams for stdout and stderr

print '\npopen3:'
proc = subprocess.Popen('cat -; echo ";to stderr" 1>&2',
                       shell=True,
                       stdin=subprocess.PIPE,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       )
stdout_value, stderr_value = proc.communicate('through stdin to stdout')
print '\tpass through:', repr(stdout_value)
print '\tstderr:', repr(stderr_value)

#Merged stdout and stderr, as with popen4:

print '\npopen4:'
proc = subprocess.Popen('cat -; echo ";to stderr" 1>&2',
                       shell=True,
                       stdin=subprocess.PIPE,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT,
                       )
stdout_value, stderr_value = proc.communicate('through stdin to stdout\n')
print '\tcombined output:', repr(stdout_value)
