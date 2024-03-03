from colorama import init, Fore
import subprocess
from modulos.sistemasoperativos import sistemasoperativos
from modulos.herramientas import herramientas


def mostrar_menu():
	subprocess.run("clear")
	print(Fore.GREEN + "==================================")
	print(Fore.WHITE + "          Termux Center")
	print(Fore.GREEN + "==================================" + Fore.WHITE)
	print("1. Instalar Sistemas Operativos")
	print("2. Instalar Herramientas")
	print("3. Sobre Termux Center")
	print("4. Salir")

def pedir_opcion():
	while True:
		try:
			opcion = int(input("Ingresa una opcion: "))
			if opcion == 1:
				sistemasoperativos()
				break
			elif opcion == 2 :
				herramientas()
				break
			elif opcion == 3 :
				break
			elif opcion == 4:
				break
			
			else:
				print("Introduce una opcion valida")
		except ValueError:
			print("Introduce una opcion valida")
		

	


mostrar_menu()
pedir_opcion()