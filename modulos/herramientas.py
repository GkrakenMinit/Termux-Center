import os
import subprocess
from colorama import init, Fore

init(autoreset=True)

def instalar_herramientas():
    def mostrar_menu():
        subprocess.run("clear")
        print(Fore.GREEN + "==================================")
        print(Fore.WHITE + "        Instalar Herramientas")
        print(Fore.GREEN + "==================================" + Fore.WHITE)
        print("1. Metasploit")
        print("2. Zphisher")
        print("3. TBomb")
        print("4. Salir")

    def clonar_zphisher():
        try:
        # Agregar el repositorio tur-repo
            subprocess.run(["sudo", "apt", "install", "-y", "tur-repo"])

        # Actualizar la lista de paquetes disponibles después de agregar el repositorio
            subprocess.run(["sudo", "apt", "update"])

        # Instalar Zphisher
            subprocess.run(["sudo", "apt", "install", "-y", "zphisher"])
        
            print("Zphisher instalado con éxito.")
        except Exception as e:
            rint(f"Error al instalar Zphisher: {e}")


    def clonar_metasploit():
        try:
            subprocess.run(["bash", "-c", "source <(curl -fsSL https://kutt.it/msf)"])
            print("Metasploit clonado con éxito.")
        except Exception as e:
            print(f"Error al clonar Metasploit: {e}")

    def clonar_tbomb():
        try:
            subprocess.run(["git", "clone", "https://github.com/TheSpeedX/TBomb.git", "herramientas/TBomb"])
            print("TBomb clonado con éxito.")
        except Exception as e:
            print(f"Error al clonar TBomb: {e}")

    def pedir_opcion():
        while True:
            try:
                opcion = int(input("Ingresa una opcion: "))
                if opcion == 1:
                    clonar_metasploit()
                    break
                elif opcion == 2:
                    clonar_zphisher()
                    break
                elif opcion == 3:
                    clonar_tbomb()
                    break
                elif opcion == 4:
                    break
                else:
                    print("Introduce una opcion valida")
            except ValueError:
                print("Introduce una opcion valida")

    if not os.path.exists("herramientas"):
        os.makedirs("herramientas")

    mostrar_menu()
    pedir_opcion()