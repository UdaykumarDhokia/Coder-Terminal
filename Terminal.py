import os
import colorama
from colorama import Fore, Back, Style
from prettytable import PrettyTable


colorama.init(autoreset=True)

print(Fore.LIGHTRED_EX + "WARNING!!!")
print("If you want to run this TERMINAL then, you have to install some important modules.")
print("1)colorama        command = pip install colorama")
print("2)PrettyTable        command = pip install PrettyTable")
print("Or you can just execute the requirements.py file")
print("If you had successfully installed the modules then type yes() or YES(), else no() or NO()")
module = input(">>>")
print("___________________________________________________________________________________________")
if module == "yes()" or module == "YES()":
    print("""
          █▀▀ █▀█ █▀▄ █▀▀ █▀█   ▀█▀ █▀▀ █▀█ █▀▄▀█ █ █▄░█ ▄▀█ █░░
          █▄▄ █▄█ █▄▀ ██▄ █▀▄   ░█░ ██▄ █▀▄ █░▀░█ █ █░▀█ █▀█ █▄▄""")
    print("                                                                 Created by - Udaykumar Dhokia")
    print(" "
          " "
          " ")
    print("___________________________________________________________________________________________")
    print(Fore.CYAN + Style.BRIGHT + "WELCOME TO THE BASIC TERMINAL")
    print("")
    print("Type /h/ to see all the commands with their functions")
    print("Type /q/ to exit or break")
    print("")
    while True:
        n = input(os.getcwd() + " ~> ")
        # CURRENT WORKING DIRECTORY
        if n == "getcwd":
            print(Fore.CYAN + os.getcwd())

        # HELP [҉҉  ]҉҉
        elif n == "/h/":
            print("")
            print("[҉҉")
            print("  To get current working directory, type " + Fore.CYAN + "getcwd")
            print("  To change directory, type " + Fore.CYAN + "chdir()")
            print("  To see all files in current directory, type " + Fore.CYAN + "showlist()")
            print("  To make a new directory, type " + Fore.CYAN + "mdir")
            print("  To make a more than one directories, type " + Fore.CYAN + "mdirs")
            print("  To rename any file, type " + Fore.CYAN + " rename")
            print("  To remove any directory, type " + Fore.CYAN + " remove")
            print("  To open a existing text(.txt) file, type " + Fore.CYAN + " opentxt()")
            print("  To create a new text(.txt) file, type " + Fore.CYAN + " opentxt(new)")
            print("  To open a existing python(.py) file, type " + Fore.CYAN + " openpy()")
            print("  To create a new python(.py) file, type " + Fore.CYAN + " openpy(new)")
            print("]҉҉")
            print("")

        # CHANGE THE DIRECTORY
        elif n == "chdir()":
            path = input("Enter the path here: ")
            os.chdir(path)
            print(Fore.CYAN + "OK!")

        # SHOW THE ITEMS IN THE DIRECTORY
        elif n == "showlist()":
            print("")
            print("[҉҉")
            data = os.listdir(os.getcwd())
            mytable = PrettyTable(["File_name", "Size in MB", "Size in bytes"])
            for i in data:
                size_MB = os.path.getsize(i) >> 20
                size_BYTES = os.path.getsize(i)
                mytable.add_row([i, size_MB, size_BYTES])
            print(mytable)
            print("]҉҉")
            print("")

        # MAKING THE DIRECTORY
        elif n == "mdir":
            name = input("Enter the name of new directory:")
            os.mkdir(name)
            print(Fore.CYAN + "OK!")

        # MAKING MULTIPLE DIRECTORIES
        elif n == "mdirs":
            n = int(input("How many directories do you want make?"))
            for i in range(n):
                name1 = input("Enter the name of directory: ")
                os.makedirs(name1)
            print(Fore.CYAN + "OK!")

        # RENAME
        elif n == "rename":
            print(Fore.CYAN + "Kindly enter the name with EXTENSION")
            value = input("Enter current name of the file: ")
            new_value = input("Enter the new name: ")
            os.rename(value, new_value)
            print(Fore.CYAN + "OK!")

        # REMOVE
        elif n == "remove":
            name = input("Enter the name of the directory: ")
            choice = input("Are you sure want delete?(y/n): ")
            if choice == "y":
                os.rmdir(name)
            elif choice == "n":
                pass
            else:
                print(Fore.RED + "Please enter valid choice...")

        # TO OPEN EXISTING TEXT FILE
        elif n == "opentxt()":
            f_name = input("Enter the name of the file: ")
            choice = input("Do want read or write(r/w)?")
            if choice == "r":
                file = open(f_name + ".txt", "r")
                value = file.read()
                print(value)
                file.close()
            elif choice == "w":
                print("If you have successfully entered your content, then TYPE", Fore.CYAN + "done()")
                while True:
                    text = input(">>>")
                    file = open(f_name + ".txt", "a")
                    if text != "done()":
                        file.write(text + "\n")
                    file.close()
                    if text == "done()":
                        break
                print(Fore.CYAN + "OK!")
            else:
                print(Fore.RED + "Error !! please enter valid choice...")

        # TO CREATE NEW TEXT FILE
        elif n == "opentxt(new)":
            f_name = input("Enter the name of the file:  ")
            print("If you have successfully entered your content, then TYPE", Fore.CYAN + "done()")
            while True:
                text = input(">>>")
                file = open(f_name + ".txt", "a")
                if text != "done()":
                    file.write(text + "\n")
                file.close()
                if text == "done()":
                    break
            print(Fore.CYAN + "OK!")

        # TO OPEN EXISTING PYTHON FILE
        elif n == "openpy()":
            f_name = input("Enter the name of the python file: ")
            print("[҉҉")
            file = open(f_name + ".py", "r")
            data = file.read()
            print(Fore.LIGHTYELLOW_EX + data)
            print("]҉҉")
            file.close()

        # TO CREATE NEW PYTHON FILE
        elif n == "openpy(new)":
            print(Fore.LIGHTRED_EX + "WARNING!!!")
            print(Fore.CYAN + "This command allows you to create the PYTHON file only. "
                              "If you want to write the code then, you have to go in IDLE or any other Coder Editor.")
            f_name = input("Enter the name of the file: ")
            file = open(f_name + ".py", "a")
            file.close()

        # QUIT
        elif n == "/q/":
            break
        else:
            print(Fore.RED + "Error !! please enter valid command...")

elif module == "no()" or module == "NO()":
    print(Fore.LIGHTRED_EX + "Kindly install now...!")

else:
    print(Fore.LIGHTRED_EX + "Please enter valid answer...!!!")