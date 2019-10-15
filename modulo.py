"""
    Script to exceute Show Commands in Cisco Device using netmiko

    # Version 1.0 12.Julio.2019
    # Heibarth Gonzalez

    # External Credit...
    # https://github.com/AlexMunoz905/Cisco-Backup-Config/blob/master/WLC.py
    # Thanks to Alex Munoz (GitHub: AlexMunoz905) for getting me started! :)
"""
import logging
import getpass
import re
import datetime
import time
import sys
from netmiko import ConnectHandler
try:
    import netmiko
except:
    print("Error Netmiko not installed - https://github.com/ktbyers/netmiko")
    sys.exit()

logging.basicConfig(
    format='[%(levelname)s] %(asctime)s %(message)s', level=logging.INFO)
logger = logging.getLogger("wlc_backup")
devices = []  # Empty array to store wlcs
files = []  # Empty array to store filenames

### Determina la Fecha y hora en la que se ejecuta el Script #####
x = datetime.datetime.now()
date = ("%s-%s-%s" % (x.year, x.month, x.day))


def Telnet(ip):
    host = ip
    un = input('Username: ')
    pw = getpass.getpass()
    print("\n")
    print("Se esta iniciando el intento de conexion " + 6*"." + "\n")
    print("Validacion de datos\nIP: "+host+"\n"+un+"\n"+pw+"\n")
    lista = []
    try:
        device = ConnectHandler(
            device_type='cisco_ios_telnet', ip=host, username=un, password=pw)
        device_str = str(device)
        lista = device_str.split()
        if len(lista) != 0:
            print('Conexion exitosa con usuario ' + un + ' en el Host ' + host)
           # Lectura del archivo de comandos IOS Switches o Router
            rutadir = "./comandos.txt"
            fp = open(rutadir, "r")
            lines = fp.read().splitlines()
            print(lines)
            fp.close()
            time.sleep(0.5)
            for line in lines:
                output = device.send_command(line)
                print(output)
            print("\n")
            print(
                "##### Se realizo la tarea de forma exitosa en el Host " + host + " #####")
            device.disconnect()
        else:
            pass
    except Exception as e:
        print('La conenxion con el host ' + host +
              ' y usuario ' + un + '; Fallo por ', e)
        f = open('EquiposDown.txt', 'a+')
        f.write(date + ' ' + host + '\n')
        f.close()
        pass


def SSH(file):
    un = input('Username: ')
    pw = getpass.getpass()
    rutadir_file = "./" + file + ".txt"
    fp = open(rutadir_file, "r")
    lines_file = fp.read().splitlines()
    print(lines_file)
    fp.close()
    for ip in lines_file:
        host = ip
        print(host)
        print("\n")
        print("Se esta iniciando el intento de conexion " + 6*"." + "\n")
        print("Validacion de datos\nIP: "+host+"\n"+un+"\n"+pw+"\n")
        lista = []
        try:
            device = ConnectHandler(device_type='cisco_ios', ip=host, username=un, password=pw)
            device_str = str(device)
            lista = device_str.split()
            if len(lista) != 0:
                print('Conexion exitosa con usuario ' + un + ' en el Host '+ host)
                ### Lectura del archivo de comandos IOS Switches o Router
                rutadir = "./comandos.txt"
                fp = open(rutadir, "r")
                lines = fp.read().splitlines()
                print(lines)
                fp.close()
                time.sleep(0.5)
                for line in lines:
                    output = device.send_command(line)
                    print ("Se esta ejecutando el comando " + 4*"! " + line + 4*" !")
                    print (output)
                print ("\n")
                print("##### Se realizo la tarea de forma exitosa en el Host " + host + " #####")
                device.disconnect()
            else:
                pass
        except Exception as e:
            print ('La conenxion con el host ' + host + ' y usuario ' + un + '; Fallo por ', e)
            f = open('EquiposDown.txt', 'a+')
            f.write(date + ' ' + host + '\n' )
            f.close()
            pass

def WLC(ip):
    host = ip
    un = input('Username: ')
    pw = getpass.getpass()
    print("\n")
    print("Se esta iniciando el intento de conexion " + 6*"." + "\n")
    print("Validacion de datos\nIP: "+host+"\n"+un+"\n"+pw+"\n")
    lista = []
    try:
        device = ConnectHandler(device_type='cisco_wlc', ip=host, username=un, password=pw, global_delay_factor=2)
        device_str = str(device)
        lista = device_str.split()
        if len(lista) != 0:
            print('Conexion exitosa con usuario ' + un + ' en el Host '+ host)
            # Lectura del archivo de comandos IOS WLC
            rutadir = "./comandos_WLC.txt"
            fp = open(rutadir, "r")
            lines = fp.read().splitlines()
            print(lines)
            fp.close()
            time.sleep(0.5)
            for line in lines:
                output = device.send_command(line)
                print (output)
            print ("\n")
            print("##### Se realizo la tarea de forma exitosa en el Host " + host + " #####")
            device.disconnect()
        else:
            return ("NO se pudo conectar al dispositivo " + host)
    except Exception as e:
        print ('La conenxion con el host ' + host + ' y usuario ' + un + '; Fallo por ', e)
        f = open('EquiposDown.txt', 'a+')
        f.write(date + ' ' + host + '\n' )
        f.close()
        pass
