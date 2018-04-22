#!/usr/bin/python3
#Esta linea nos da info del sistema en el que se ejecuta el sistema
import sys
system = sys.platform
print(system)
#Nos da la fecha del dia
from datetime import date
hoy = date.today()
print(hoy.strftime("%m-%d-%y. Hoy es %d de %B."))
####Definimos las funciones antes para saber como se va a comportar el programa
def kernel(topic):
	print("Kernel ok?")
	print("¿Que necesitas saber?")
	duda = str(input())
	if duda in ['que es','que significa']:
		fo = open("kernel.txt", "r+")
		leer = fo.read()
		print("¿Que es?: \n", leer)
		fo.close
	elif duda in ["historia","Historia","History"]:
		fo = open("history.txt", "r+")
		leer = fo.read()
		print(leer)
		fo.close

def compilar(topic):
	print("Compilacion ok?")
	print("¿Cual es tu duda?")
	dudas = str(input())
	if dudas in ['como compilo','programa en c'] :
		print("Solo escribe en una terminal -gcc programa.c -o programa-\n")
		pass
	elif dudas in ['que es GCC','GCC?']:
		fo = open("gcc.txt","r+")
		leer = fo.read()
		print("Pues es: ",leer)
		fo.close
	elif dudas in ['make?',"make"]:
		fo = open("make.txt","r+")
		leer = fo.read()
		print(leer)
		fo.close

def server(topic):
	print("Server ok?")
	print("¿Que quieres saber?")
	duda = str(input())
	if duda in ["Instalar","como montar un servidor","instalar","como crear"]:
		print("Te recomiendo que instales apache2\n Para Debian/Ubuntu:\n'sudo apt install apache2*'")
		

print("Sistema Experto en GNU/Linux")
print("¿Que Distribucion GNU/Linux usas?")
dist = str(input()) #Pide una palabra para empezar

#Primeros Filtros de la entrada del sistema
if dist in ["que", "Linux?", "linux?","mmmmmm","que es linux?","que es linux"]:	
		print("\nNo lo sabes?\n")
		fo = open("linux.txt","r+")
		leer = fo.read()
		print("Bueno pues linux es: ", leer)
		fo.close
		exit()

elif dist in ["Fedora","Suse","fedora","suse"]:
		print("Sabes tu sistema de binarios?")
		q = str(input())
		if q in ["no","No"]:
			fo = open("RPM.txt","r+")
			leer = fo.read()
			print("Pues para estos sistemas es:\n",leer)
			fo.close
			q = "Si"

elif dist in ["Debian","Ubuntu","debian","ubuntu"]:
		print("Sabes tu sistema de binarios?")
		q = str(input())
		if q in ["no","No"]:
			fo = open("DPKG.txt","r+")
			leer = fo.read()
			print("Pues para estos sistemas es:\n",leer)
			fo.close
			q = "Si"
			
if q in ["Si","si"]:
	 print("¿Cual es tu problema o duda?")
	 topic = str(input())
###Segunos filtros de la pregunta
if topic in ['nucleo','Kernel','kernel']:
	kernel(topic)

if topic in ['Compilacion','GCC',"compilar"]:
	compilar(topic)

if topic in ["Server","Servidor","servidores"]:
	server(topic)

print("Otra duda?")
topico = str(input())

if topico in ["no","No"]:
	exit()
elif topico in ["Si","si"]:
	exit()

print("Algo mas?\n")
ser = str(input())

if ser in ["No", "no"]:
	exit()
elif ser in ["Si", "si"]:
	exit()