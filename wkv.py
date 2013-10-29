#!/usr/bin/python

# WKeyView
# Version: v0.3
# Author: nestor.2005 [at] gmail.com
#
# Test 1234


import os
import sys


#Asistente WKeyView
def help():
        print "\n########################################################################################################"
        print
        print "[-] WKeyView v0.3"
        print 
        print "[-] After type the name of the wifi, your password is in row 15. Assigned to 'psk' (Pre-shared key)"
        print "[-] Example:\n\tpsk=testing\n\tIn this case your internet password is 'testing'.\n\n"
        print "[-] Errors:\n\t- 'Error reading FILE ESSID': It means that the name is invalid or the file does not exist."
        print "\t- 'Error reading MOVE. Invalid command': It means that the command that you type does not exist."
        print 
        print "########################################################################################################"


#Busca los archivos de wifi guardadas y printea las wifi encontradas
def wifi(direc):
        files = os.listdir(direc)
        print "\nThe found files are:"
        for element in files:
                print "\t[-] " + element + "\n"


#Lee el archivo y lo printea en pantalla
def ReadTxt(direc, name):
        try:
                i = 1
                text = open(direc + name,'r')
                line = text.readline()
                while line != "":
                        print "\t%d) "%i + line
                        line = text.readline()
                        i = i + 1 #para numerar las lineas
                text.close()
        except:
                print "\t[-] Error reading '%s' ESSID"%name
                exit()


#Pide comandos y los ejecuta de acuerdo a lo escrito por el usuario.
def main(direc):
        move = raw_input("To search the wifi, type 'show'. Or type 'help' for assistance.\n")


        if move == 'help':
                help()
                wifi(direc)
        elif move == 'show':
                wifi(direc)
        else:
                print "\n[-] Error reading '%s'. Invalid command." %move
                exit()

        NameWifi = raw_input("Enter the name of the file:")
        
        print "\n\t######################### " + NameWifi + " #########################"
        ReadTxt(PATH, NameWifi)
        print "\t######################### " + NameWifi + " #########################"


PATH = '/etc/NetworkManager/system-connections/'

#Comprueba si sos root
if os.geteuid() != 0:
        print "You must have root privileges to run this script."
        sys.exit(1)

main(PATH)

