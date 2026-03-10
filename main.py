import os
import time
import subprocess
import sys
import tkinter as tk

#  предупреждение
if os.path.exists(f"./warn.txt"):
    with open(f"./warn.txt", "r", encoding="utf-8") as f:
        content = f.read()
        if content == "0":
            with open(f"./warn.txt", "w", encoding="utf-8") as f:
                f.write("1")
            root = tk.Tk()
            root.title("Warn")
            root.geometry("300x300")
            lab = tk.Label(root, text="WARNING, PROGRAMM ISNT MY, THIS IS FLOWSEALS")
            def delete():
                root.destroy()
            button = tk.Button(root, text="OK", command=delete)
            lab.pack()
            button.pack()
            root.mainloop()
        else:
            print()
else:
    with open(f"./warn.txt", "w", encoding="utf-8") as f:
        f.write("1")
        root = tk.Tk()
        root.title("Warn")
        root.geometry("300x300")
        lab = tk.Label(root, text="WARNING, PROGRAMM ISNT MY, THIS IS FLOWSEALS")
        def delete():
            root.destroy()
        button = tk.Button(root, text="OK", command=delete)
        lab.pack()
        button.pack()
        root.mainloop()

os.environ['PYTHONIOENCODING'] = 'utf-8'

if sys.platform == 'win32':
    os.system('chcp 65001 > nul')

if getattr(sys, 'frozen', False):
    script_dir = os.path.dirname(sys.executable)
else:
    script_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_dir)

with open(f"log.txt", "w", encoding="UTF-8") as file:
    file.write("started")
    file.write("\n")

def zapret_on():
    time.sleep(1)
    print("Выберите alt:")
    zapret = input("Введите alt:")
    file = f"./{zapret}.bat"
    subprocess.run(file, shell=True, cwd=script_dir)
    time.sleep(1)
with open(f"log.txt", "a", encoding="UTF-8") as file:
    file.write("create zapret_on")
    file.write("\n")

def zapret_off():
    time.sleep(1)
    subprocess.run(f"taskkill /F /IM winws.exe", shell=True)
    time.sleep(1)
    with open(f"log.txt", "a", encoding="UTF-8") as file:
        file.write("zapret off")
        file.write("\n")
with open(f"log.txt", "a", encoding="UTF-8") as file:
    file.write("create zapret_off")
    file.write("\n")

def menu():
    print("""    включить запрет:1
    выключить запрет:2
    Выйти:3
    вписать сайт в листы:4
    вписать в ip сайта в листы:5""")
    vibor = int(input())
    if vibor == 1:
        zapret_on()
    elif vibor == 2:
        zapret_off()
    elif vibor == 3:
        with open(f"log.txt", "a", encoding="UTF-8") as file:
            file.write("finished")
        exit()
    elif vibor == 4:
        with open(f"./lists/list-general.txt", "a", encoding="UTF-8") as file:
            site = input("введите сайт:")
            file.write(f"\n{site}")
    elif vibor == 5:
        with open(f"./lists/ipset-all.txt", "a", encoding="UTF-8") as file:
            site_ip = input("введите ip сайта:")
            file.write(f"\n{site_ip}")
        with open(f"./lists/ipset-exclude.txt", "a", encoding="UTF-8") as file:
            site_ip = input("введите ip сайта:")
            file.write(f"\n{site_ip}")
    elif vibor == 52:
        subprocess.run(f"maxresdefault.jpg", shell=True, cwd=script_dir)
    menu()

menu()

