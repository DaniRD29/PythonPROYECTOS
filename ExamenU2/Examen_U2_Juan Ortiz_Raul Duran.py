# EXAMEN DE POO UNIDAD 2, CREANDO UN PROGRAMA PARA UNA TAQUERIA (NOMBRE FICTICIO: TACONTENTO)
# AUTORES: RAUL DANILO DURAN DZUL Y JUAN CARLOS ORTIZ SALAS
# FECHA: 31/03/23

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk

# *************************************CONEXION CON LA BASE DE DATOS Y FUNCIONES DE ESTA*************************

from tkinter import message

def IngresarDatos():
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="tacontento1"
    )

    fcursor = db.cursor()

    sql = "INSERT INTO pedidos (user, contra) VALUES ('{0}', '{1}')".format(
        user_entry.get(), contra_entry.get())

    try:
        fcursor.execute(sql)
        db.commit()
        ventana_registro.destroy()
    except:
        db.rollback()
        messagebox.showinfo(
            message="dou! No se pudo realizar el registro", title="AVISO DE REGISTRO")
    db.close()


def ValidacionDatos():
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="tacontento1"
    )

    fcursor = db.cursor()

    fcursor.execute("SELECT contra FROM pedidos WHERE user='" +
                    user_verify.get()+"' and contra='"+contra_verify.get()+"'")

    if (fcursor.fetchall()):
        menu_emp()
    else:
        messagebox.showinfo(title="INICIO DE SESION INCORRECTA",
                            message="EL USUARIO Y CONTRASENA NO SON CORRECTAS :/")

    db.close()


def tomarpedido():

    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="tacontento2"
    )

    fcursor = db.cursor()

    sql = "INSERT INTO pedidos (tort, carn, sals, cantida, complemen) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(
        tortilla.get(), carne.get(), salsas.get(), cantidad.get(), complemento.get())

    try:
        fcursor.execute(sql)
        db.commit()
        recibo()
    except:
        db.rollback()
        messagebox.showinfo(
            message="dou! No se pudo realizar el registro", title="AVISO DE REGISTRO")
    db.close()


def consultar_pedido():

    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="tacontento2"
    )

    fcursor = db.cursor()
    consulta = "SELECT * FROM pedidos ORDER BY id desc"
    fcursor.execute(consulta)
    # Y los resultados los almacenamos en la variable datos.
    datos = fcursor.fetchall()
    for i in datos:
        lista_pedidos.insert("", 0, text=i[0], values=(
            i[1], i[2], i[3], i[4], i[5]))


# ********************CREAMOS PRIMERO UNA CLASE CON POLIFORMISMO PARA HACER LOS CALCULOS Y SACAR EL IMPORTE DEL PEDIDO******************************************


class calculos ():
    def __init__(self, carne_tomar, cantidad_tomar, precio, orden):
        self.carne_tomar = str(carne_tomar)
        self.cantidad_tomar = str(cantidad_tomar)
        self.precio = int(precio)
        self.orden = int(orden)

    def cobro(self):
        pass


class cobrar(calculos):
    def cobro(self):
        if carne.get() == "Pastor (Precio = 15.00$ c/u)" or carne.get() == "Asada (Precio = 15.00$ c/u)" or carne.get() == "Tripa (Precio = 15.00$ c/u)":
            self.precio = 15
        else:
            self.precio = 20

        if cantidad.get() == "Orden Individual (2 Tacos)":
            self.orden = 2
        elif cantidad.get() == "Orden de Pareja (4 Tacos)":
            self.orden = 4
        elif cantidad.get() == "Orden Amigos (8 Tacos)":
            self.orden = 8
        elif cantidad.get() == "Orden Familiar (16 Tacos)":
            self.orden = 16

        return ("Importe: $ {} pesos".format(self.precio*self.orden))

# *******************VENTANA DONDE EL USUARIO ELIJE SI REALIZAR EL PEDIDO O ACCEDER COMO EMPLEADO*******************************


def venp():
    global ven
    ven = tk.Tk()
    ven.title("TACONTENTO")
    ven.geometry("700x500")
    ven.iconbitmap("EXAMEN_UNIDAD2_JUANORTIZ_RAULDURAN/favicon.ico")

    img6 = PhotoImage(file="EXAMEN_UNIDAD2_JUANORTIZ_RAULDURAN/IMG6.png")
    Label(ven, image=img6).pack()

    buton1 = Button(ven, text="CLIENTES", font=("Arial", 20),
                    fg="snow", bg="red", command=eleccion)
    buton1.place(width=250, height=90, x=225, y=100)
    buton2 = Button(ven, text="EMPLEADOS", font=("Arial", 20),
                    fg="snow", bg="red", command=bottpress2)
    buton2.place(width=250, height=90, x=225, y=200)
    boton_close = tk.Button(ven, text="Salir", font=(
        "Arial", 10), fg="white", bg="deep pink", command=ven.destroy)
    boton_close.place(width=150, height=30, x=480, y=450)
    ven.resizable(0, 0)
    ven.mainloop()

# *****************************VENTANAS DE CLIENTE*******************************************************************
# *****************************VENTANA DONDE EL CLIENTE REALIZA EL PEDIDO*********************************************


def eleccion():
    global cl
    cl = tk.Toplevel(ven)
    cl.title("Pedido")
    cl.geometry("500x600")
    cl.iconbitmap("EXAMEN_UNIDAD2_JUANORTIZ_RAULDURAN/favicon.ico")

    img4 = PhotoImage(file="EXAMEN_UNIDAD2_JUANORTIZ_RAULDURAN/IMG4.gif")
    Label(cl, image=img4).pack()
    global tortilla
    global carne
    global salsas
    global cantidad
    global complemento

    tortilla = ttk.Combobox(cl, state="readonly", values=[
                            "Maiz", "Harina", "Azul"], font=("calibri light", 15))
    tortilla.place(x=150, y=150, width=300, height=30)

    carne = ttk.Combobox(cl, state="readonly", values=[
        "Pastor (Precio = 15.00$ c/u)", "Asada (Precio = 15.00$ c/u)", "Tripa (Precio = 15.00$ c/u)", "Mixto (Precio = 20.00$ c/u)", "Lengua (Precio = 20.00$ c/u)", "Suadero (Precio = 20.00$ c/u)", "Chorizo (Precio = 20.00$ c/u)"], font=("calibri light", 15))
    carne.place(x=150, y=200, width=300, height=30)

    salsas = ttk.Combobox(cl, state="readonly", values=[
        "Salsa Roja (Xtra Picante)", "Salsa Verde", "Salsa de Chiles Mixtos", "Salsa de Ajo", "Salsa de Tomate", "Sin salsas"], font=("calibri light", 15))
    salsas.place(x=150, y=250, width=300, height=30)

    cantidad = ttk.Combobox(cl, state="readonly", values=[
                            "Orden Individual (2 Tacos)", "Orden de Pareja (4 Tacos)", "Orden Amigos (8 Tacos)", "Orden Familiar (16 Tacos)"], font=("calibri light", 15))
    cantidad.place(x=150, y=300, width=300, height=30)

    complemento = ttk.Combobox(cl, state="readonly", values=[
        "Nopal", "Piña", "Aguacate", "Pimientos", "Pico de gallo", "Queso", "Sin complementos"], font=("calibri light", 15))
    complemento.place(x=150, y=350, width=300, height=30)

    Label(cl, text="Tortilla", fg="snow", bg="red3", width="12",
          height="2", font=("corbel", 12)).place(x=30, y=144)

    Label(cl, text="Carne", fg="snow", bg="red3", width="12",
          height="2", font=("corbel", 12)).place(x=30, y=194)

    Label(cl, text="Salsas", fg="snow", bg="red3", width="12",
          height="2", font=("corbel", 12)).place(x=30, y=244)

    Label(cl, text="Cantidad", fg="snow", bg="red3", width="12",
          height="2", font=("corbel", 12)).place(x=30, y=294)

    Label(cl, text="Complementos", fg="snow", bg="red3", width="12",
          height="2", font=("corbel", 12)).place(x=30, y=344)

    button_pedir = tk.Button(
        cl, text="Realizar pedido", command=validar)
    button_pedir.place(x=200, y=425, width=200, height=30)

    cl.resizable(0, 0)
    cl.mainloop()


# ***************************************VENTANA DEL RECIBO DEL CLIENTE*************************************


def recibo():
    global vent_recibo
    global take

    vent_recibo = tk.Toplevel(ven)
    vent_recibo.title("Recibo")
    vent_recibo.geometry("400x400")

    vent_recibo.iconbitmap("EXAMEN_UNIDAD2_JUANORTIZ_RAULDURAN/favicon.ico")

    img3 = PhotoImage(file="EXAMEN_UNIDAD2_JUANORTIZ_RAULDURAN/IMG3.gif")
    Label(vent_recibo, image=img3).pack()

    take = cobrar(carne.get(), cantidad.get(), 0, 0)

    Label(vent_recibo, text=take.cobro(), fg="grey1", bg="red2", width="20",
          height="3", font=("corbel", 12)).place(x=105, y=300)

    Label(vent_recibo, fg="grey1", text="Su orden de tacos ha sido registrada \n Tipo de tortilla: "+tortilla.get() +
          " \n Carne del taco: "+carne.get()+"\n Salsa de la orden: "+salsas.get()+"\n Tamano de la orden :"+cantidad.get()+"\n Complemento del taco: "+complemento.get()+"\n GRACIAS POR SU COMPRA", width="35", height="8", font=("corbel", 12)).place(x=40, y=30)

    Label(vent_recibo, text="Esperando... ", fg="grey1", bg="DarkOrange2", width="20",
          height="3", font=("corbel", 12)).place(x=105, y=200)

    vent_recibo.resizable(0, 0)
    cl.destroy()
    vent_recibo.mainloop()


def validar():
    if tortilla.get() == "" or carne.get() == "" or salsas.get() == "" or cantidad.get() == "" or complemento.get() == "":
        messagebox.showinfo(
            message="Algun campo sigue vacio, vuelva a intentar", title="Aviso")
    else:
        tomarpedido()

# ***********************************VENTANAS DEL EMPLEADO*******************************************************
# ***********************VENTANA DE INICIAR SESION PARA EL EMPLEADO EN TURNO*************************************


def bottpress2():
    global vn3
    vn3 = tk.Toplevel(ven)
    vn3.title("Empleados")
    vn3.config(width=700, height=500)
    vn3.iconbitmap("EXAMEN_UNIDAD2_JUANORTIZ_RAULDURAN/favicon.ico")

    img1 = PhotoImage(file="EXAMEN_UNIDAD2_JUANORTIZ_RAULDURAN/IMG1.gif")
    Label(vn3, image=img1).pack()

    global user_verify
    global contra_verify
    user_verify = tk.Entry(vn3)
    contra_verify = tk.Entry(vn3, show="●")

    # Mas botones con diseño
    Label(vn3, text="INICIE SESION", font=(
        "Arial", 15), bg="khaki1").place(x=225, y=100)
    Label(vn3, text="USUARIO:", font=("Arial", 15),
          bg="khaki1").place(x=120, y=150)
    user_verify.place(x=225, y=150, width=250, height=30)

    # Eliminacion de dato ingresado

    user_verify.bind("<Button-1>", lambda e: user_verify.delete(0, END))

    Label(vn3, text="CONTRASEÑA:", font=(
        "Arial", 15), bg="khaki1").place(x=70, y=250)
    contra_verify.place(x=225, y=250, width=250, height=30)

    # Eliminacion de dato ingresado

    contra_verify.bind("<Button-1>", lambda e: contra_verify.delete(0, END))

    Label(vn3, text="¿ERES NUEVO?", font=(
        "Arial", 10), bg="khaki1").place(x=300, y=300)

    buton3 = Button(vn3, text="REGISTRATE", font=("Arial", 15),
                    fg="snow", bg="deep pink", command=registrar)
    buton3.place(width=250, height=40, x=225, y=325)

    buton_ini = Button(vn3, text="INICIAR SESION", font=("Arial", 15),
                       fg="snow", bg="deep pink", command=ValidacionDatos)
    buton_ini.place(width=250, height=40, x=225, y=370)

    boton_close = tk.Button(vn3, text="Cerrar ventana", font=(
        "Arial"), fg="white", bg="deep pink", command=vn3.destroy)
    boton_close.place(x=530, y=450)
    vn3.resizable(0, 0)
    vn3.mainloop()

# *********************************MENU DEL EMPLEADO PARA REGISTRARSE************************************************


def registrar():
    global ventana_registro
    ventana_registro = tk.Toplevel(ven)
    ventana_registro.title("Registro de empleado")
    ventana_registro.geometry("400x300")

    ventana_registro.iconbitmap(
        "EXAMEN_UNIDAD2_JUANORTIZ_RAULDURAN/favicon.ico")

    img2 = PhotoImage(file="EXAMEN_UNIDAD2_JUANORTIZ_RAULDURAN/IMG2.gif")
    Label(ventana_registro, image=img2).pack()

    global user_entry
    global contra_entry

    user_entry = StringVar()
    contra_entry = StringVar()

    user_entry = Entry(ventana_registro, font=("calibri light", 14))
    user_entry.place(x=150, y=102, width=175, height=30)
    contra_entry = Entry(ventana_registro, show="●")
    contra_entry.place(x=150, y=152, width=175, height=30)

    Label(ventana_registro, text="Usuario", fg="snow", bg="red3", width="12",
          height="2", font=("corbel", 10)).place(x=50, y=100)

    Label(ventana_registro, text="contraseña", fg="snow", bg="red3", width="12",
          height="2", font=("corbel", 10)).place(x=50, y=150)

    Label(ventana_registro, text="Registrate a Tacontento :)", fg="gray1", width="20",
          height="2", font=("calibri light", 20)).place(x=50, y=20)

    boton_registrar = Button(
        ventana_registro,
        text="¡Registrarse!",
        command=IngresarDatos
    )
    boton_registrar.place(x=195, y=200)

    ventana_registro.mainloop()

# ************************VENTANA DE MENU PARA EL EMPLEADO, DONDE SE VISUALIZAN LOS PEDIDOS******************


def menu_emp():
    global vent_emp
    vent_emp = tk.Toplevel(ven)
    vent_emp.title("Menu para empleados y pedidos")
    vent_emp.geometry("1280x700")

    vent_emp.iconbitmap("EXAMEN_UNIDAD2_JUANORTIZ_RAULDURAN/favicon.ico")

    img5 = PhotoImage(file="EXAMEN_UNIDAD2_JUANORTIZ_RAULDURAN/IMG5.png")
    Label(vent_emp, image=img5).place(x=0, y=0)

    global tabla_pedidos
    global lista_pedidos

    barra_menus = tk.Menu(vent_emp)
    menu_archivo = tk.Menu(barra_menus, tearoff=0)
    ventana_menu = tk.Menu(barra_menus, tearoff=0)

    barra_menus.add_cascade(menu=menu_archivo, label="Empleados")
    menu_archivo.add_command(label="Añadir empleado", command=registrar)

    barra_menus.add_cascade(menu=ventana_menu, label="Ventana")
    ventana_menu.add_command(
        label="tamaño original (1280x700)", command=tamano)
    vent_emp.config(menu=barra_menus)

    # CREAR LA TABLA DE PEDIDOS

    tabla_pedidos = LabelFrame(
        vent_emp, text=" LISTADO DE PRODUCTOS: ")
    tabla_pedidos.grid(row=7, column=0, columnspan=5, padx=20, pady=25)
    tabla_pedidos.place(x=10, y=200)

    lista_pedidos = ttk.Treeview(
        tabla_pedidos, height=10, columns=("#1", "#2", "#3", "#4", "#",))
    lista_pedidos.grid(row=7, column=0, columnspan=4, padx=20, pady=20)

    lista_pedidos.heading("#0", text="ID", anchor=CENTER)
    lista_pedidos.heading("#1", text="Tortilla", anchor=CENTER)
    lista_pedidos.heading("#2", text="Carne", anchor=CENTER)
    lista_pedidos.heading("#3", text="Salsa", anchor=CENTER)
    lista_pedidos.heading("#4", text="Orden", anchor=CENTER)
    lista_pedidos.heading("#5", text="Complemento", anchor=CENTER)

    consultar_pedido()

    button_acept = Button(
        vent_emp, text="Terminar los pedidos", width="30", height="4", bg="green2", command=aceptar_pedido)
    button_acept.place(x=1000, y=40)

    move_up = Scrollbar(tabla_pedidos, command=lista_pedidos.yview)
    move_up.grid(row=7, column=4, sticky="nsew")
    lista_pedidos.config(yscrollcommand=move_up.set)

    vent_emp.mainloop()

# **********************************FUNCIONES PARA LA VENTANA DEL MENU************************************


def aceptar_pedido():
    Label(vent_recibo, text="Pedido aceptado", fg="grey1", bg="green2", width="20",
          height="3", font=("corbel", 12)).place(x=105, y=200)


def tamano():
    vent_emp.geometry("1280x700")


venp()