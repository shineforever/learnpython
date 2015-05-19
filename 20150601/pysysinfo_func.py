#!/usr/bin/env python
# -*- coding:utf-8 -*-

#A System information Gathering Script

import subprocess

#subprocess.call(["some_command","some_argument","another_argument_or_path"])
#subprocess.call(command,shell=True)

#Command 1
def uname_func():
	uname="uname"
	uname_arg="-a"
	print ("Gathering system information with %s command:\n" % uname)
	subprocess.call([uname,uname_arg])

#subprocess.call("uname -a",shell=True)

#Command 2
def disk_func():
	diskspace="df"
	diskspace_arg="-h"
	print ("Gathering diskspace information %s command:\n" % diskspace)
	#subprocess.call([diskspace,diskspace_arg])
	subprocess.call("df -h",shell=True)
#Main function that call other functions
def main():
	uname_func()
	disk_func()

main()

