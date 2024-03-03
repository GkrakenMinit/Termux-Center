import subprocess
from colorama import init, Fore

init(autoreset=True)

def sistemasoperativos():
    def mostrar_menu():
        subprocess.run("clear")
        print(Fore.GREEN + "==================================")
        print(Fore.WHITE + "       Sistemas Operativos")
        print(Fore.GREEN + "==================================")
        print("1. Debian")
        print("2. Arch Linux")
        print("3. Ubuntu")
        print("4. Alpine")
        print("5. Artix Linux")
        print("6. Salir")

    def instalar_y_ejecutar(distro):
        instalar_proot_distro(distro)
        run_distro(distro)

    def instalar_proot_distro(alias):
        subprocess.run(["proot-distro", "install", alias])

    def run_distro(distro):
        filename = distro
        with open(filename, 'w') as file:
            file.write(f"proot-distro login {distro}")
        subprocess.run(["chmod", "777", filename])
        subprocess.run(["mv", filename, "../../usr/bin"])

    def pedir_opcion():
        opciones = {
            1: "debian",
            2: "archlinux",
            3: "ubuntu-lts",
            4: "alpine",
            5: "artix",
            6: None
        }
        while True:
            try:
                opcion = int(input("Ingresa una opcion: "))
                if opcion in opciones:
                    distro = opciones[opcion]
                    if distro is None:
                        break
                    instalar_y_ejecutar(distro)
                    break
                else:
                    print("Introduce una opcion valida")
            except ValueError:
                print("Introduce una opcion valida")

    mostrar_menu()
    pedir_opcion()