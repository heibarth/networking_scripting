"""
    Script to exceute Show Commands in Cisco Device using netmiko

    # Version 2.0 14.Agosto.2019
    # Heibarth Gonzalez

    # External Credit...
    # https://github.com/AlexMunoz905/Cisco-Backup-Config/blob/master/backup-config-menu.py
    # Thanks to Alex Munoz (GitHub: AlexMunoz905) for getting me started! :)
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import modulo

def menu():
    print("Por favor seleccione el tipo de dispositivo en el cual desea enviar los comandos\n")
    print("Debe ingresar solo el numeros segun aplique\n")
    print("1. IOS Router and Switch con Telnet")
    print("2. IOS Router and Switch con SSH")
    print("3. WLC")
    print("")
    print("4. Exit")
    print(" ")
    OurInput = input("Ingrese el numero asociado al tipo de conexion: ")
    if OurInput == "1":
        print("Ha seleccionado Telnet")
        print("Por favor ingrese el nombre del archivo con las IPs de los dispositivos a conectar: ")
        ip = input('Nombre del Archivo: ')
        modulo.Telnet(ip)
    elif OurInput == "2":
        print("Ha seleccionado la Opcion 2. Conexion SSH")
        print("Por favor ingrese el nombre del archivo con las IPs de los dispositivos a conectar: ")
        file = input('Nombre del Archivo: ')
        modulo.SSH(file)
    elif OurInput == "3":
        print("Ha seleccionado SSH hacia un WLC")
        print("Por favor ingrese el nombre del archivo con las IPs de los dispositivos a conectar: ")
        ip = input('Nombre del Archivo: ')
        modulo.WLC(ip)
    elif OurInput == "4":
        print("Gracias por Visitarnos")
        return
    elif (OurInput == ""):
        print("\n")
        print("#"*44)
        print("### No ha ingresado ningun valor         ###")
        print("### Por favor ingrese una entrada valida ###")
        print("#"*44)
        return menu()
    elif (OurInput != "1" or OurInput != "2" or OurInput != "3"):
        print("### Ha ingresado el siguiente valor: "+ OurInput +" ###")
        print("### Por favor ingrese una entrada valida ###")
        print("#"*50)
        return menu()

menu()