#!/usr/bin/python

# WKeyView
# Version: v0.2
# Author: nestor.2005 [at] gmail.com
#
# Test 123


import os
import sys


#Asistente WKeyView
def help():
        print "\n########################################################################################################"
        print
        print "[-] WKeyView v0.2"
        print 
        print "[-] After type the name of the wifi, your password is in row 29. Assigned to the 'psk' (Pre-shared key)"
        print "[-] Example:\n\tpsk=testing\n\tIn this case your internet password is 'testing'.\n\n"
        print "[-] Errors:\n\t'Error reading FILE ESSID': It means that the name is invalid or the file does not exist."
        print "\t'Error reading MOVE. Invalid command': It means that the command that you type does not exist."
        print 
        print "########################################################################################################"


#Busca los archivos de wifi guardadas y printea las wifi encontradas
def wifi():
	files = os.listdir('/etc/NetworkManager/system-connections')
	print "\nThe found files are:"
	for element in files:
		print "\t[-] " + element + "\n"


#Lee el archivo y lo printea en pantalla
def ReadTxt():
	try:
		text = open('/etc/NetworkManager/system-connections/' + NameWifi,'r')
		line = text.readline()
		while line != "":
			print "\t" + line
			line = text.readline()
		text.close()
	except:
		print "\t[-] Error reading '%s' ESSID"%NameWifi
		exit()



#Comprueba si sos root
if os.geteuid() != 0:
    	print "You must have root privileges to run this script."
    	sys.exit(1)	

move = raw_input("To search the wifi, type 'show'. Or type 'help' for assistance.\n")

if move == 'help':
        help()
        wifi()
elif move == 'show':
        wifi()
else:
        print "[-] Error reading '%s'. Invalid command." %move
        exit()


NameWifi = raw_input("Enter the name of the wifi:")

print "\n\t######################### " + NameWifi + " #########################"
ReadTxt()
print "\t######################### " + NameWifi + " #########################"
