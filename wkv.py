#!/usr/bin/python
#
#
# WKeyView
#
# Author: Nestor Paez
# Email: nestor.2005 [at] gmail.com
# Twitter: twitter.com/ntpaez
#

import os
import sys
from termcolor import colored #sudo pip install termcolor

#Asistente WKeyView
def help():
        print
        print "########################################################################################################"
        print 
        print "[-] WKeyView"
        print "[-] For the moment, this script is only available on Linux. For more information contact the author."
        print "[-] E-mail: nestor.2005 [at] gmail.com
        print 
        print "[-] Examples:"
        print "         - psk=testing                           (In this case your internet password is 'testing')"
        print "         - psk=PUlp__FiCt10n                     (Here, the password is 'PUlp__FiCt10n')"
        print "         - psk=HasKel_Is_n0t_aN_leNguAgE         (Password: 'HasKel_Is_n0t_aN_leNguAgE')"
        print 
        print "[-] Errors:"
        print "         - 'Error reading FILE ESSID': It means that the name is invalid or the file does not exist."
        print "         - 'Error reading MOVE command': Means that the command that you typed is invalid."
        print "         - 'ImportError: No module named termcolor': This script uses the library 'termcolor'."
        print 
        print "########################################################################################################"

#Busca los archivos de wifi guardadas y printea las wifi encontradas
def wifi(direc):
        files = os.listdir(direc)
        print
        print "The found files are:"
        for element in files:
                print "         [-] " + element + "\n"

#Lee el archivo y lo printea en pantalla
def ReadTxt(direc, name):
        try:
                text = open(direc + name,'r')
                for lines in text:
                        line2 = lines.strip()
                        if line2.startswith("psk"):
                                print
                                print "         ######################### " + name + " #########################"
                                print 
                                print colored("         ESSID PASSWORD: %s"%line2,"blue")
                                print 
                                print "         ######################### " + name + " #########################"
                text.close()
        except:
                print colored("[-] Error reading '%s' ESSID"%name, "red")
                exit()

#Bucle para nueva busqueda
def next(move, direc):
        while move == "Y":
                main(direc)
        if move == "N":
                exit()
        else:
                print
                print colored("[-] Error reading '%s'. Invalid command." %move, "red")
                exit()

#Pide comandos y los ejecuta de acuerdo a lo escrito por el usuario.
def main(direc):
        move = raw_input("To search the wifi, type 'show'. Or type 'help' for assistance: ")

        if move == 'help':
                help()
                wifi(direc)
        elif move == 'show':
                wifi(direc)
        else:
                print colored("\n[-] Error reading '%s'. Invalid command." %move, "red")
                exit()

        NameWifi = raw_input("Enter the name of the file: ")
        ReadTxt(direc, NameWifi)
        
        NextMove = raw_input("\nDo you wanna do a new search? Y/N: ")
        next(NextMove, direc)



#Comprueba si sos root
if os.geteuid() != 0:
        print "You must have root privileges to run this script."
        sys.exit(1)

PATH = '/etc/NetworkManager/system-connections/'
main(PATH)
