import os
import time
import subprocess
import sys
import tkinter as tk
import ctypes

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
    print("включить запрет:1\nвыключить запрет:2\nВыйти:3")
    vibor = int(input())
    if vibor == 1:
        zapret_on()
    elif vibor == 2:
        zapret_off()
    elif vibor == 3:
        with open(f"log.txt", "a", encoding="UTF-8") as file:
            file.write("finished")
        exit()
    elif vibor == 52:
        subprocess.run(f"maxresdefault.jpg", shell=True, cwd=script_dir)
    menu()

menu()

