#!/usr/bin/python
#
#
# WKeyView
#
# Version: v0.3
# Author: Nestor Paez
# Email: nestor.2005 [at] gmail.com
# Twitter: twitter.com/ntpaez
#

import os
import sys
from termcolor import colored #sudo pip install termcolor


#Asistente WKeyView
def help():
        print "\n########################################################################################################"
        print
        print "[-] WKeyView v0.3"
        print "[-] For now, this script only works on Linux. For more information contact the author."
        print 
        print "[-] Example:\n\t- psk=testing\t\t (In this case your internet password is 'testing')"
        print "\t- psk=PUlp__FiCt10n\t (Here, the password is 'PUlp__FiCt10n')\n"
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
                text = open(direc + name,'r')
                for lines in text:
                        line2 = lines.strip()
                        if line2.startswith("psk"):
                                print "\n\t######################### " + name + " #########################"
                                print ""
                                print colored("\tESSID PASSWORD: %s"%line2,"red")
                                print ""
                                print "\t######################### " + name + " #########################"
                text.close()
                
                #lista.tito
                #    line2 = lines.split(' ')
                #    for line in line2:
                #        if line.startswith("psk"):
                #Arregla que crashee cuando el ESSID tenga espacio. (revisar)

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

        NameWifi = raw_input("Enter the name of the file: ")
        ReadTxt(direc, NameWifi)
        
        NextMove = raw_input("\nDo you wanna do a new search? Y/N: ")
        next(NextMove, direc)


#Mini bucle para nueva busqueda
def next(move, direc):
        while move == "Y":
                main(direc)
        if move == "N":
                exit()
        else:
                print "\n[-] Error reading '%s'. Invalid command." %move
                exit()


#Comprueba si sos root
if os.geteuid() != 0:
        print "You must have root privileges to run this script."
        sys.exit(1)


PATH = '/etc/NetworkManager/system-connections/'
main(PATH)

