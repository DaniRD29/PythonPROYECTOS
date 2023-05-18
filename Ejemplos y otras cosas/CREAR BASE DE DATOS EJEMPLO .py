# EJEMPLO PARA CONECTAR BASE DE DATOS EN XAMPP by danigod


import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = db.cursor()

try:
    cursor.execute("CREATE DATABASE IF NOT EXIST ejemplo;")
    print("SI SE CREO")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS login (id INT AUTO_INCREMENT PRIMARY KEY, user VARCHAR(255), contra VARCHAR(225))")
except:
    print("NO SE CREO")


# PAGINA DE CODIGOS PARA LA BASE DE DATOS

try:
    cursor.execute("DROP DATABASE ejemplo;")
    print("SI SE elimino")
except:
    print("NO SE elimino")

# https://programacionfacil.org/blog/bases-de-datos-mysql-con-python/
