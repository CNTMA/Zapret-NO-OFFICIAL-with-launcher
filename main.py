import os
import time
import subprocess
import sys
import tkinter as tk

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
    root2 = tk.Tk()
    root2.title("ZAPRET")
    root2.geometry("300x300")
    lab2 = tk.Label(root2, text="выберите alt:")
    entry2 = tk.Entry(root2)
    lab2.pack()
    entry2.pack()
    def func_on():
        zapret = entry2.get()
        file = f"./{zapret}.bat"
        subprocess.run(file, shell=True, cwd=script_dir)
        time.sleep(1)
        root2.destroy()
        menu()
    button2 = tk.Button(root2, text="OK", command=func_on)
    button2.pack()

    button2 = tk.Button(root2, text="OK", command=func_on)
with open(f"log.txt", "a", encoding="UTF-8") as file:
    file.write("create zapret_on")
    file.write("\n")

def zapret_off():
    root3 = tk.Tk()
    root3.title("ZAPRET")
    root3.geometry("300x300")
    lab3 = tk.Label(root3, text="выключение...:")
    lab3.pack()
    subprocess.run(f"taskkill /F /IM winws.exe", shell=True)
    time.sleep(2)
    root3.destroy()
    menu()

    with open(f"log.txt", "a", encoding="UTF-8") as file:
        file.write("create zapret_off")
        file.write("\n")

def menu():
    root1 = tk.Tk()
    root1.title("MENU")
    root1.geometry("300x300")
    lab1 = tk.Label(root1, text="включить запрет:1\nвыключить запрет:2\nвыйти:3\nвписать в листы сайт:4\nвписать сайт в ipset:5")
    def delete1():
        global vibor
        vibor = input_tk.get()
        root1.destroy()
    button1 = tk.Button(root1, text="OK", command=delete1)
    input_tk = tk.Entry(root1)
    input_tk.pack()
    lab1.pack()
    button1.pack()
    root1.mainloop()
    if vibor == "1":
        zapret_on()
    elif vibor == "2":
        zapret_off()
    elif vibor == "3":
        with open(f"log.txt", "a", encoding="UTF-8") as file:
            file.write("finished")
        exit()
    elif vibor == "4":
        root3 = tk.Tk()
        root3.title("ZAPRET")
        root3.geometry("300x300")
        lab3 = tk.Label(root3, text="выберите caйт:")
        entry3 = tk.Entry(root3)
        lab3.pack()
        entry3.pack()

        def func_on2():
            with open(f"./lists/list-general.txt", "a", encoding="UTF-8") as file:
                file.write(f"\n{entry3.get()}")
                menu()
                root3.destroy()

        button3 = tk.Button(root3, text="OK", command=func_on2)
        button3.pack()
    elif vibor == "5":
        root4 = tk.Tk()
        root4.title("ZAPRET")
        root4.geometry("300x300")
        lab4 = tk.Label(root4, text="выберите caйт:")
        entry4 = tk.Entry(root4)
        lab4.pack()
        entry4.pack()

        def func_on1():
            with open(f"./lists/list-general.txt", "a", encoding="UTF-8") as file:
                with open(f"./lists/ipset-all.txt", "a", encoding="UTF-8") as file:
                    site_ip = input("введите ip сайта:")
                    file.write(f"\n{entry3.get()}")
                with open(f"./lists/ipset-exclude.txt", "a", encoding="UTF-8") as file:
                    file.write(f"\n{entry3.get()}")
                menu()
                root4.destroy()

        button4 = tk.Button(root4, text="OK", command=func_on1)
        button4.pack()

    elif vibor == "52":
        subprocess.run(f"maxresdefault.jpg", shell=True, cwd=script_dir)
    menu()

menu()

