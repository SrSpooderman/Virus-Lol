import os
import tkinter as tk
import time
bucle = 1
programa = "RiotClientServices.exe"
while bucle == 1:
    lectura = os.popen('wmic process get description, processid').read()
    if programa in lectura:
        print("se esta ejecuando")
        time.sleep(600)
        ventana = tk.Tk()
        ventana.attributes('-fullscreen', True)
        ventana.configure(background="purple")
        os.system("shutdown /s /t 1")
        ventana.mainloop()
    else:
        print("no se esta ejecutando")