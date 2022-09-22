"""•Haga un listado con todos los datos dado el número de alumnos
•Imprima por pantalla el listado de alumnos (todos los datos)
•Muestre los alumnos de mayor y menor edad
•Imprima el listado de las de las niñas y los niños
•Busque un alumno por el número cédula
•Elimine los alumnos"""
global lista
import sys
import os
lista = list()
class Alumno:
	#defino datos del alumno
	ced= "" #dato string
	nombre= "" #dato string
	edad= 0 #dato numerico
	gen= ""
def registrarAlumno():
	a=Alumno()
	a.ced= input("║ Ingrese cedula: ")
	while not(len(a.ced) == 10 and a.ced.isdigit()):
            print('Procura que sean numeros y que sean 10 caracteres')
            a.ced=input('║Ingrese cedula: ')
	a.nombre= input("║ Ingrese nombre: ")
	a.edad= int(input("║ Ingrese edad: "))
	while not(a.edad>0 and a.edad<=120):
            print('Edad fuera de rango')
            a.edad=int(input('║Ingrese edad : '))
	a.gen= input("║ Ingrese genero | Masculino o Femenino |: ")
	a.gene= a.gen.lower()
	if a.gene == "masculino" or a.gene == "femenino":
	    lista.append(a)
	else:
	    datomalo()
	   
def listarAlumno():
    print("CEDULA -  NOMBRE  - EDAD - GENERO ")
    for a in lista:
	    print (a.ced, "-", a.nombre, "-", a.edad, "-", a.gene)
def mayoredad():
    for a in lista:
        if a.edad>=18:
            print (a.ced, "-", a.nombre, "-", a.edad, "-", a.gene)
        
def menoredad():
    for a in lista:
        if a.edad<=18:
            print (a.ced, "-", a.nombre, "-", a.edad, "-", a.gene)
        
def buscarAlumno():
	print("Busqueda de alumno")
	ced=input("Ingrese numero de cedula: ")
	for a in lista:
	    if a.ced==ced:
	        print (a.ced, "-", a.nombre, "-", a.edad, "-", a.gene)
def salir():
    print("Adios")
    sys.exit()
def datomalo():
    print("DATO INCORRECTO- INTENTELO NUEVAMENTE")
    menu()
    sys.exit()
def varones():
    #print(lista for a in lista if a.nombre(-1)=='o'and a.nombre(-1)=='el' and a.nombre(-1)=='EL' and a.nombre(-1)=='O')
    for a in lista:
        if a.gene=='masculino':
            print (a.ced, "-", a.nombre, "-", a.edad, "-", a.gene)
def damas():
    for a in lista:
        print("Mujeres: ")
        if a.gene=='femenino':
            print (a.ced, "-", a.nombre, "-", a.edad, "-", a.gene)
def eliminarAlumno():
    print("Eliminar alumno")
    ced=input("Ingrese numero de cedula del almuno a elminar: ")
    for a in lista:
	    if a.ced==ced:
	      print ("Se ha borrado a : ", a.ced, "-", a.nombre, "-", a.edad, "-", a.gene)
	      lista.remove(a)
def menu():
	opc= 0
	salirr=9
	while opc !=salirr:
		print("╔════════════════MENU══════════════════╗")
		print("║ 1. REGISTRAR ALUMNO                  ║")
		print("║ 2. MOSTRAR LISTADO GENERAL DE ALMUNOS║")
		print("║ 3. MOSTRAR ALUMNOS MAYORES DE EDAD   ║")
		print("║ 4. MOSTRAR ALUMNOS MENORES DE EDAD   ║")
		print("║ 5. MOSTRAR VARONES                   ║")
		print("║ 6. MOSTRAR DAMAS                     ║")
		print("║ 7. BUSCAR ALUMNO POR CEDULA          ║")
		print("║ 8. ELIMINAR ALUMNO                   ║")
		print("║ 9. SALIR                             ║")
		print("╚══════════════════════════════════════╝")
		opc= int(input("DIGITE OPCION ►► "))
		if opc == 1:
		    registrarAlumno()
		    os.system('clear')
		elif opc ==2:
		    listarAlumno()
		elif opc ==3:
			mayoredad()
		elif opc==4:
			menoredad()
		elif opc==5:
		    varones()
		elif opc==6:
		    damas()
		elif opc==7:
		    buscarAlumno()
		elif opc==8:
		    eliminarAlumno()
		elif opc==9:
		    salir()
menu()