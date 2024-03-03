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

def verificar_instalacion_y_instalar():
    # Verificar si proot-distro está instalado
    resultado = subprocess.run(["dpkg", "-l", "proot-distro"], capture_output=True, text=True)
    if "proot-distro" not in resultado.stdout:
        # Si proot-distro no está instalado, instalarlo
        print("proot-distro no está instalado. Instalando...")
        subprocess.run(["apt", "install", "proot-distro", "-y"])
        print("proot-distro instalado con éxito.")
    else:
        sistemasoperativos()

def pedir_opcion():
	while True:
		try:
			opcion = int(input("Ingresa una opcion: "))
			if opcion == 1:
				verificar_instalacion_y_instalar()
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