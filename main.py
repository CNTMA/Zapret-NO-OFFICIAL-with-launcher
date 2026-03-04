import os
import time
import subprocess
import sys

if getattr(sys, 'frozen', False):
    script_dir = os.path.dirname(sys.executable)
else:
    script_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_dir)

with open(f"./.log.txt", "w", encoding="UTF-8") as file:
    file.write("started")
    file.write("\n")

def zapret_on():
    time.sleep(1)
    print("Выберите alt:")
    zapret = input("Введите alt:")
    file = f"./{zapret}.bat"
    subprocess.run(file, shell=True, cwd=script_dir)
    time.sleep(1)
    with open(f"./.log.txt", "w", encoding="UTF-8") as file:
        file.write("create zapret_on")
        file.write("\n")

def menu():
    print("включить запрет:1\nвыключить запрет:2")
    vibor = int(input())
    if vibor == 1:
        zapret_on()
    elif vibor == 2:
        zapret_on()
    menu()

menu()

with open(f"./.log.txt", "a", encoding="UTF-8") as file:
    file.write("finished")
