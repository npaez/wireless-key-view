#!/usr/bin/python

# WKeyView
# Version: v0.1
# Author: nestor.2005 [at] gmail.com

import os
import sys

#Comprueba si sos root
if os.geteuid() != 0:
  print "You must have root privileges to run this script."
  sys.exit(1)

#Asistente WKeyView
def help():
	print "\n\tWKeyView v0.1"
	print "\n\tAfter type the name of the wifi, your password is in row 29. Assigned to the 'psk' (Pre-shared key)"
	print "\tExample:\n\tpsk=testing\n\tIn this case your wifi's password is 'testing'.\n\n"

#Busca los archivos de wifi guardadas.
files = os.listdir('/etc/NetworkManager/system-connections')

#Printea las wifis encontradas.
def wifi():
	files
	print "\nThe wifi found are:"
	for element in files:
		print "\t~ " + element + "\n"


#Lee el archivo y lo printea en pantalla
def ReadTxt():
  text = open('/etc/NetworkManager/system-connections/' + NameWifi,'r') #for 'NameWifi' see row 47
  line = text.readline()
  while line != "":
    print "\t" + line
    line = text.readline()

  text.close()

NextMove = raw_input("To search the wifi, type 'show'. Or type 'help' for assistance.\n")
while (NextMove != "help" or NextMove != "show"):
	NextMove = raw_input("Ingrese un nuevo movimiento: ")
	if NextMove == "help":
		help()
		break
	if NextMove == "show":
		break




wifi()		
NameWifi = raw_input("Enter the name of the wifi: ")






#Testea que el nombre sea valido- AH LISTO QUE VILLERO
i = 0
while i < len(files):
  while NameWifi != files[i]:
		i = i + 1
		if i == len(files):
			i = i - len(files)
			print "Error: El nombre del archivo es incorrecto."
			NameWifi = raw_input("Enter the name of the wifi: ")
	else:
		break


print "\n\t######################### " + NameWifi + " #########################"
ReadTxt()
print "\t######################### " + NameWifi + " #########################"
