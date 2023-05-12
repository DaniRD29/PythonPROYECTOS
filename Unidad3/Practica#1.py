#Importaciones
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import pymysql

#Ventana Principal
ven=Tk()
ven.geometry("350x200")
ven.title("Practica 1")
ven.config(bg="pale green")
Label(ven,text="APLICANDO LO YA VISTO", font=("Arial",10), bg="pale green").grid(row=0,column=1)

Label(ven,text="Id:",bg="pale green").grid(row=1, column=0, padx=5, pady=5)
id=tk.Entry(ven)
id.grid(row=1, column=1, padx=2, pady=5)
id.bind("<Button-1>", lambda e: id.delete(0, END))

Label(ven,text="Nombre:",bg="pale green").grid(row=2, column=0, padx=5, pady=5)
nom=tk.Entry(ven)
nom.grid(row=2, column=1, padx=2, pady=5)
nom.bind("<Button-1>", lambda e: nom.delete(0, END))

Label(ven,text="Edad:",bg="pale green").grid(row=3, column=0, padx=5, pady=5)
ag=tk.Entry(ven)
ag.grid(row=3, column=1, padx=2, pady=5)
ag.bind("<Button-1>", lambda e: ag.delete(0, END))

Label(ven,text="Correo:",bg="pale green").grid(row=4, column=0, padx=5, pady=5)
gm=tk.Entry(ven)
gm.grid(row=4, column=1, padx=2, pady=5)
gm.bind("<Button-1>", lambda e: gm.delete(0, END))

ven.resizable(0,0)
ven.mainloop()