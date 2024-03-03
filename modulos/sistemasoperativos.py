from colorama import init, Fore
import subprocess

def sistemasoperativos():
    def mostrar_menu():
            subprocess.run("clear")
            print(Fore.GREEN + "==================================")
            print(Fore.WHITE + "       Sistemas Operativos")
            print(Fore.GREEN + "==================================" + Fore.WHITE)
            print("1. Debian")
            print("2. Arch Linux")
            print("3. Ubuntu")
            print("4. Alpine")
            print("5. Artix Linux")
            print("6. Salir")

    def instalar_proot_distro(alias):
        subprocess.run(["proot-distro", "install", alias])

    def pedir_opcion():
        while True:
            try:
                opcion = int(input("Ingresa una opcion: "))
                if opcion == 1:
                    instalar_proot_distro("debian")
                    break
                elif opcion == 2 :
                    instalar_proot_distro("archlinux")
                    break
                elif opcion == 3 :
                    instalar_proot_distro("ubuntu-lts")
                    break   
                elif opcion == 4:
                    instalar_proot_distro("alpine")
                    break
                elif opcion == 5:
                    instalar_proot_distro("artix")
                elif opcion == 6:
                    break
                else:
                    print("Introduce una opcion valida")
            except ValueError:
                print("Introduce una opcion valida")
    mostrar_menu()
    pedir_opcion()

	
