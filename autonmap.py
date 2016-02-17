#!/usr/bin/python
import sys, os, time
from subprocess import call

print "----------------------------------------------------------------"
print " [+] NMap Automatic Network/Host Scanner [+]"
print " By: Alan Cao"
print "----------------------------------------------------------------"

print "Options:"
print "1)Simple Scan\n2)Intense Scan\n3)IPv6 Scan\n4)Ping Scan\n5)Fast Scan\n6)UDP Scan"
print "7)Port Selection\n8)Port Scan (TCP SYN)\n9)OS Detection Scan"
print "10)Standard Service Detection\n11)Heartbleed SSL Vulnerability Scan\n12)IP Info"
print "13)Help\n14)Go Back"

option = input("[>] Choose An Option, Young Padawan: ")
target = raw_input(" [>] Enter Target IP/Hostname for Scanning: (none if you exiting)")

if option == 1:
	call(["nmap", "-v", target])
elif option == 2:
	call(["nmap", "-T4", "-A", target])
elif option == 3:
	call(["nmap", "-6", target])
elif option == 4:
	call(["nmap", "-sP", target])
elif option == 5:
	call(["nmap", "-F", target])
elif option == 6:
	call(["nmap", "-sU", target])
elif option == 7:
	call(["nmap", "-p", target])
elif option == 8:
	call(["nmap", "-sS", target])
elif option == 9:
	call(["nmap", "-A", target])
elif option == 10:
	call(["nmap", "-sV", target])
elif option == 11:
	call(["nmap", "-sV", "-p 443", "--script=ssl-heartbleed", target])
elif option == 12:
	call(["nmap", "--script=asn-query", "whois", "ip-geolocation-maxmind", target])
elif option == 13:
	call(["gedit", "help.txt"])
elif option == 14:
	call(["python","menu.py"])

