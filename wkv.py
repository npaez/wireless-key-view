#!/usr/bin/python

# WKeyView
# Version: ???
# Author: un boludo


import os
import sys

#Comprueba si sos root
if os.geteuid() != 0:
    print "You must have root privileges to run this script."
    sys.exit(1)

#Asistente WKeyView
def help():
	print "\n\tWKeyView v?.?"
	print "\n\tAfter type the name of the wifi, your password is in row 29. Assigned to the 'psk' (Pre-shared key)"
	print "\tExample:\n\tpsk=testing\n\tIn this case your wifi's password is 'testing'.\n\n"

#Busca los archivos de wifi guardadas y printea las wifi encontradas
def wifi():
	files = os.listdir('/etc/NetworkManager/system-connections')
	print "\nThe wifi found are:"
	for element in files:
		print "\t~ " + element + "\n"


#Lee el archivo y lo printea en pantalla
def ReadTxt():
    text=open('/etc/NetworkManager/system-connections/' + wifi,'r')
    line=text.readline()
    while line != "":
        print "\t" + line
        line=text.readline()

    text.close()

move = raw_input("To search the wifi, type 'show'. Or type 'help' for assistance.\n")

if move == "help":
	help()


wifi()		
wifi = raw_input("Enter the name of the wifi:")

print "\n\t######################### " + wifi + " #########################"
ReadTxt()
print "\t######################### " + wifi + " #########################"
