from colorama import init, Fore
import subprocess

def herramientas():
    def mostrar_menu():
            subprocess.run("clear")
            print(Fore.GREEN + "==================================")
            print(Fore.WHITE + "       Herramienntas")
            print(Fore.GREEN + "==================================" + Fore.WHITE)
            print("1. Debian")
            print("2. Arch Linux")
            print("3. Ubuntu")
            print("4. Manjaro")
            print("5. Fedora")
            print("6. Salir")
    def pedir_opcion():
        while True:
            try:
                opcion = int(input("Ingresa una opcion: "))
                if opcion == 1:
                    print("Instalando")
                elif opcion == 2 :
                    print("Instalando")
                elif opcion == 3 :
                    print("Instalando")
				        
                elif opcion == 4:
                    print("Instalando")
                elif opcion == 5:
                    print("Instalando")
                elif opcion == 6:
                    break
                else:
                    print("Introduce una opcion valida")
            except ValueError:
                print("Introduce una opcion valida")
    mostrar_menu()
    pedir_opcion()

	
