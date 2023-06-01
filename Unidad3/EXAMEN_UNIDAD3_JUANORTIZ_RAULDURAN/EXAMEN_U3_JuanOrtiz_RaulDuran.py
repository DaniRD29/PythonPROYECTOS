# EXAMEN DE POO UNIDAD 2, CREANDO UN PROGRAMA PARA UNA TAQUERIA (NOMBRE FICTICIO: TACONTENTO)
# AUTORES: RAUL DANILO DURAN DZUL Y JUAN CARLOS ORTIZ SALAS
# FECHA: 31/03/23

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk

#***************************************CREAR LA BASE DE DATOS Y LA TABLA***************************************

db = pymysql.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = db.cursor()

try:
    cursor.execute("CREATE DATABASE tacontento1;")
    print("SI SE CREO")
except:
    print("NO SE CREO")

def create_tables1():
    db = pymysql.connect(
      host="localhost",
      user="root",
      password="",
      db="tacontento1"
    )

    cursor = db.cursor()

    try:
        cursor.execute("CREATE TABLE login (id INT AUTO_INCREMENT PRIMARY KEY, user VARCHAR(255), contra VARCHAR(225))")
        cursor.execute("CREATE TABLE pedidos (id INT AUTO_INCREMENT PRIMARY KEY, tort VARCHAR(255), carn VARCHAR(255), sals VARCHAR(255), cantida VARCHAR(255), complemen VARCHAR(255))")
        print("TABLAS CREADAS CORRECTAMENTE")
    except:
        print("TABLAS NO CREADAS")
        return

create_tables1()


# *************************************CONEXION CON LA BASE DE DATOS Y FUNCIONES DE ESTA*************************

def validar_busqueda():
    global multi
    while True:
        try:
            multi = int()
            multi = 0
            multi = int(busqueda.get())
            break
        except ValueError:
            messagebox.showerror(
                title="AVISO", message="EL VALOR INGRESADO NO ES UN NUMERO")
            return
    buscar_ped()


def validacion_de_login1():
    if user_verify.get()=="Usuario" or contra_verify.get()=="Contraseña":
        messagebox.showerror(title="Aviso", message="Algún campo sigue vacío, vuelva a intentar")
    else:
        ValidacionDatos()

def validacion_de_login2():
    if user_entry.get()=="Usuario" or contra_entry.get()=="Contraseña":
        messagebox.showerror(title="Aviso", message="Algún campo sigue vacío, vuelva a intentar")
    else:
        IngresarDatos()

def IngresarDatos():
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="tacontento1"
    )

    fcursor = db.cursor()

    sql = "INSERT INTO login (user, contra) VALUES ('{0}', '{1}')".format(
        user_entry.get(), contra_entry.get())

    try:
        fcursor.execute(sql)
        db.commit()
        des4()
    except:
        db.rollback()
        messagebox.showerror(
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

    fcursor.execute("SELECT contra FROM login WHERE user='" +
                    user_verify.get()+"' and contra='"+contra_verify.get()+"'")

    if (fcursor.fetchall()):
        vn3.withdraw()
        menu_emp()
    else:
        messagebox.showerror(title="INICIO DE SESION INCORRECTA",
                            message="EL USUARIO Y CONTRASENA NO SON CORRECTAS :/")

    db.close()


def tomarpedido():

    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="tacontento1"
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
        messagebox.showerror(
            message="dou! No se pudo realizar el registro", title="AVISO DE REGISTRO")
        return
    db.close()


def consultar_pedido():

    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="tacontento1"
    )

    fcursor = db.cursor()
    consulta = "SELECT * FROM pedidos ORDER BY id desc"
    fcursor.execute(consulta)
    # Y los resultados los almacenamos en la variable datos.
    datos = fcursor.fetchall()
    for i in datos:
        lista_pedidos.insert("", 0, text=i[0], values=(
            i[1], i[2], i[3], i[4], i[5]))
        
        #aqui se hizo un cambio en los valores xd 


# ***********************************CRUD******************************************

def actualizar_tabla():
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="tacontento1"
    )

    filacrud = lista_pedidos.get_children()
    for item in filacrud:
        lista_pedidos.delete(item)
    
    fcursor = db.cursor()
    consulta = "SELECT * FROM pedidos ORDER BY id desc"
    fcursor.execute(consulta)
    datos = fcursor.fetchall()
    for i in datos:
        lista_pedidos.insert("", 0, text=i[0], values=(
            i[1], i[2], i[3], i[4], i[5]))

def eliminar_elemento():

    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="tacontento1"
    )

    try:
        lista_pedidos.item(lista_pedidos.selection())['values'][0]
    except IndexError as e:
        # mensaje de error y return para validar que se selecionen los datos
        messagebox.showerror(
            "AVISO", "POR FAVOR, PRIMERO SELECCIONA UN ELEMENTO DE LA TABLA")
        return

    # aqui uso DELETE FROM para eliminar datos, todo esto se aplica de misma forma a los demas CRUD
    sql = "DELETE FROM pedidos WHERE id = '{0}'".format(lista_pedidos.item(lista_pedidos.selection())['text'])

    preg = messagebox.askquestion(
        message="¿ESTÁS SEGURO DE QUERER ELIMINAR ESTE ELEMENTO?", title="AVISO")
    if preg == 'yes':
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        actualizar_tabla()
    else:
        messagebox.showerror(message="ERROR AL ELIMINAR", title="AVISO")
        return

def prueba ():

    iid_t = lista_pedidos.item(lista_pedidos.selection())['text']
    producto_t = lista_pedidos.item(lista_pedidos.selection())['values'][0]
    cantidad_t = lista_pedidos.item(lista_pedidos.selection())['values'][1]
    marca_t = lista_pedidos.item(lista_pedidos.selection())['values'][2]
    estado_t = lista_pedidos.item(lista_pedidos.selection())['values'][3]
    precio_t = lista_pedidos.item(lista_pedidos.selection())['values'][4]

    print(iid_t)
    print(producto_t)
    print(cantidad_t)
    print(marca_t)
    print(estado_t)
    print(precio_t)

def modificar_ped ():

    global iid_mod

    try:
        lista_pedidos.item(lista_pedidos.selection())['values'][0]
    except IndexError as e:
        # mensaje de error y return para validar que se selecionen los datos
        messagebox.showerror(
            "AVISO", "POR FAVOR, PRIMERO SELECCIONA UN ELEMENTO DE LA TABLA")
        return
    
    iid_mod=lista_pedidos.item(lista_pedidos.selection())['text']
    
    ventana_modificar()
    
def modificar_ped2():

    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="tacontento1"
    )

    # aqui uso DELETE FROM para eliminar datos, todo esto se aplica de misma forma a los demas CRUD
    sql = "UPDATE pedidos SET tort = '{0}', carn = '{1}', sals = '{2}', cantida = '{3}', complemen = '{4}' WHERE id = '{5}'".format( tortilla_mod.get(), carne_mod.get(), salsas_mod.get(), cantidad_mod.get(), complemento_mod.get(), iid_mod)
    
    preg = messagebox.askquestion(
        message="¿ESTÁS SEGURO DE QUERER MODIFICAR ESTE ELEMENTO?", title="AVISO")

    if preg == 'yes':
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        actualizar_tabla()
        ven_modify.destroy()
    else:
        messagebox.showerror(message="ERROR AL MODIFICAR", title="AVISO")
        return
    
def buscar_ped():

    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="tacontento1"
    )

    fcursor = db.cursor()
    consulta = "SELECT * FROM pedidos WHERE id = {}".format(busqueda.get())

    try:
       fcursor.execute(consulta)

       filacrud = lista_pedidos.get_children()
       for item in filacrud:
          lista_pedidos.delete(item)

       datos = fcursor.fetchall()

       for i in datos:
         lista_pedidos.insert("", 0, text=i[0], values=(i[1], i[2], i[3], i[4], i[5]))
    except:
       messagebox.showerror(title="ERROR", message="Dato erroneo ingresado, vuelva a intentar")
       return
   
#-------Buscar Tipos de carne--------

def buscar_T():

    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="tacontento1"
    )

    fcursor = db.cursor()
    consulta = "SELECT * FROM pedidos WHERE carn='{0}'".format((busqueda2.get()))

    try:
       fcursor.execute(consulta)

       filacrud = lista_pedidos.get_children()
       for item in filacrud:
          lista_pedidos.delete(item)

       datos = fcursor.fetchall()

       for i in datos:
         lista_pedidos.insert("", 0, text=i[0], values=(i[1], i[2], i[3], i[4], i[5]))
    except:
       messagebox.showerror(title="ERROR", message="Dato erroneo ingresado, vuelva a intentar")
       return

#*************************CLASES PARA EL RECIBO DEL CLIENTE Y USOS PARA DISENO*****************************

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


def bg_user(event):
    texto_actual = user_verify.get()
    if texto_actual == "Usuario":
        user_verify.delete(0, END)
        user_verify.config(fg='black')
    elif texto_actual == "":
        user_verify.insert(0, "Usuario")
        user_verify.config(fg='gray78')

def bg_contra(event):
    texto_actual = contra_verify.get()
    if texto_actual == "Contraseña":
        contra_verify.delete(0, END)
        contra_verify.config(fg='black', show="●")
    elif texto_actual == "":
        contra_verify.insert(0, "Contraseña")
        contra_verify.config(fg='gray78', show=())

def bg_user2(event):
    texto_actual = user_entry.get()
    if texto_actual == "Usuario":
        user_entry.delete(0, END)
        user_entry.config(fg='black')
    elif texto_actual == "":
        user_entry.insert(0, "Usuario")
        user_entry.config(fg='gray78')

def bg_contra2(event):
    texto_actual = contra_entry.get()
    if texto_actual == "Contraseña":
        contra_entry.delete(0, END)
        contra_entry.config(fg='black', show="●")
    elif texto_actual == "":
        contra_entry.insert(0, "Contraseña")
        contra_entry.config(fg='gray78', show=())

def validate_entry2(a, b):

    if len(b) > 12:
        return False
    
    return a.isalpha()

def validate_entry(a, b):

    if len(b) > 12:
        return False
    
    return a.isidentifier()

def validate_entry3(a, b):

    if len(b) > 3:
        return False
    
    return a.isdecimal()


# *******************VENTANA DONDE EL USUARIO ELIJE SI REALIZAR EL PEDIDO O ACCEDER COMO EMPLEADO*******************************


def venp():

    try:
        cl.withdraw()
        vn3.withdraw()
    except Exception:
        pass

    global ven
    ven = tk.Tk()
    ven.title("TACONTENTO")
    ven.geometry("700x500")
    ven.iconbitmap("EXAMEN_UNIDAD3_JUANORTIZ_RAULDURAN/favicon.ico")

    img6 = PhotoImage(file="EXAMEN_UNIDAD3_JUANORTIZ_RAULDURAN/IMG3.gif")
    Label(ven, image=img6).pack()

    buton1 = Button(ven, text="CLIENTES", font=("segoe ui black", 25),
                    fg="snow", bg="maroon", command=eleccion)
    buton1.place(width=250, height=90, x=225, y=200)
    buton2 = Button(ven, text="EMPLEADOS", font=("segoe ui black", 25),
                    fg="snow", bg="maroon", command=bottpress2)
    buton2.place(width=250, height=90, x=225, y=300)
    boton_close = tk.Button(ven, text="Salir", font=(
        "segoe ui black", 10), fg="maroon", bg="gold", command=ven.destroy)
    boton_close.place(width=150, height=30, x=275, y=400)

    ven.resizable(0, 0)
    ven.mainloop()

# *****************************VENTANAS DE CLIENTE*******************************************************************
# *****************************VENTANA DONDE EL CLIENTE REALIZA EL PEDIDO*********************************************


def eleccion():
    try:
        ven.withdraw()
        vn3.withdraw()
    except Exception:
        pass

    global cl
    cl = tk.Toplevel(ven)
    cl.title("Pedido")
    cl.geometry("500x600")
    cl.iconbitmap("EXAMEN_UNIDAD3_JUANORTIZ_RAULDURAN/favicon.ico")

    img4 = PhotoImage(file="EXAMEN_UNIDAD3_JUANORTIZ_RAULDURAN/IMG5.gif")
    Label(cl, image=img4).pack()

    global tortilla
    global carne
    global salsas
    global cantidad
    global complemento

    tortilla = ttk.Combobox(cl, state="readonly", values=[
                            "Maíz", "Harina", "Azul"], font=("calibri light", 15))
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

    Label(cl, text="Tortilla", fg="snow", bg="maroon", width="12",
          height="2", font=("segoe ui black", 10)).place(x=30, y=144)

    Label(cl, text="Carne", fg="snow", bg="maroon", width="12",
          height="2", font=("segoe ui black", 10)).place(x=30, y=194)

    Label(cl, text="Salsas", fg="snow", bg="maroon", width="12",
          height="2", font=("segoe ui black", 10)).place(x=30, y=244)

    Label(cl, text="Cantidad", fg="snow", bg="maroon", width="12",
          height="2", font=("segoe ui black", 10)).place(x=30, y=294)

    Label(cl, text="Complementos", fg="snow", bg="maroon", width="12",
          height="2", font=("segoe ui black", 10)).place(x=30, y=344)

    button_pedir = tk.Button(
        cl, text="Realizar pedido", command=validar, fg="snow", font= ("segoe ui black", 8), bg= "maroon")
    button_pedir.place(x=205, y=425, width=200, height=30)

    cl.protocol("WM_DELETE_WINDOW", des1)
    cl.resizable(0, 0)
    cl.mainloop()

#********************************************CIERRE DE VENTANAS***********************************

def des1 ():
    try:
       cl.destroy()
       ven.deiconify()
    except Exception:
        pass

def des2 ():
    try:
       vent_recibo.destroy()
       ven.deiconify()
    except Exception:
        pass

def des3 ():
    try:
       vn3.destroy()
       ven.deiconify()
    except Exception:
        pass

def des4 ():
    try:
       ventana_registro.destroy()
       vn3.deiconify()
    except Exception:
        pass

def des5 ():
    try:
       vent_emp.destroy()
       ven.deiconify()
    except Exception:
        pass



# ***************************************VENTANA DEL RECIBO DEL CLIENTE*************************************


def recibo():

    global vent_recibo
    global take

    vent_recibo = tk.Toplevel(ven)
    vent_recibo.title("Recibo")
    vent_recibo.geometry("400x400")

    vent_recibo.iconbitmap("EXAMEN_UNIDAD3_JUANORTIZ_RAULDURAN/favicon.ico")

    img3 = PhotoImage(file="EXAMEN_UNIDAD3_JUANORTIZ_RAULDURAN/IMG4.gif")
    Label(vent_recibo, image=img3).pack()

    take = cobrar(carne.get(), cantidad.get(), 0, 0)

    Label(vent_recibo, text=take.cobro(), fg="snow", bg="maroon", width="20",
          height="3", font=("segoe ui black", 10)).place(x=105, y=310)

    Label(vent_recibo, fg="grey1", text="Su orden de tacos ha sido registrada \n Tipo de tortilla: "+tortilla.get() +
          " \n Carne del taco: "+carne.get()+"\n Salsa de la orden: "+salsas.get()+"\n Tamano de la orden :"+cantidad.get()+"\n Complemento del taco: "+complemento.get()+"\n GRACIAS POR SU COMPRA", width="35", height="8", font=("corbel", 12)).place(x=40, y=30)

    Label(vent_recibo, text="Pedido recibido ", fg="snow", bg="DarkOrange2", width="20",
          height="3", font=("segoe ui black", 10)).place(x=105, y=240)

    vent_recibo.resizable(0, 0)
    cl.destroy()
    vent_recibo.protocol("WM_DELETE_WINDOW", des2)
    vent_recibo.mainloop()


def validar():
    if tortilla.get() == "" or carne.get() == "" or salsas.get() == "" or cantidad.get() == "" or complemento.get() == "":
        messagebox.showerror(
            message="Algún campo sigue vacío, vuelva a intentar", title="Aviso")
    else:
        tomarpedido()

def validar2():
    if tortilla_mod.get() == "" or carne_mod.get() == "" or salsas_mod.get() == "" or cantidad_mod.get() == "" or complemento_mod.get() == "":
        messagebox.showerror(
            message="Algún campo sigue vacío, vuelva a intentar", title="Aviso")
    else:
        modificar_ped2()
# ***********************************VENTANAS DEL EMPLEADO*******************************************************
# ***********************VENTANA DE INICIAR SESION PARA EL EMPLEADO EN TURNO*************************************


def bottpress2():

    try:
        ven.withdraw()
        ventana_registro.withdraw()
        cl.withdraw()
    except Exception:
        pass


    global vn3
    vn3 = tk.Toplevel(ven)
    vn3.title("Bienvenido, inicie sesión")
    vn3.geometry("500x350")
    vn3.iconbitmap("EXAMEN_UNIDAD3_JUANORTIZ_RAULDURAN/favicon.ico")

    img1 = PhotoImage(file="EXAMEN_UNIDAD3_JUANORTIZ_RAULDURAN/IMG1.gif")
    Label(vn3, image=img1).pack()

    global user_verify
    global contra_verify

    user_valid=StringVar()
    contra_valid=StringVar()

    user_verify = tk.Entry(vn3, bg="ghost white", validate="key", validatecommand=(vn3.register(validate_entry2), "%S", "%P"), textvariable=user_valid, justify="center", fg="gray78")
    user_verify.insert(0,'Usuario')
    user_verify.bind("<FocusIn>", bg_user)
    user_verify.bind("<FocusOut>", bg_user)
    contra_verify = tk.Entry(vn3, bg="ghost white", validate="key", validatecommand=(vn3.register(validate_entry), "%S", "%P"), textvariable=contra_valid, justify="center", fg="gray78")
    contra_verify.insert(0,'Contraseña')
    contra_verify.bind("<FocusIn>", bg_contra)
    contra_verify.bind("<FocusOut>", bg_contra)


    # Mas botones con diseño
    Label(vn3, bg="ghost white", text="Bienvenido", font=(
        "Segoe ui black", 16), fg="maroon").place(x=70, y=50)
    
    user_verify.place(x=35, y=100, width=180, height=25)
    contra_verify.place(x=35, y=140, width=180, height=25)

    buton3 = Button(vn3, text="¿Eres nuevo?", font=("segoe ui black", 8),
                    fg="snow", bg="maroon", command=registrar)
    buton3.place(width=180, height=25, x=35, y=220)

    buton_ini = Button(vn3, text="INICIAR SESIÓN", font=("segoe ui black", 8),
                       fg="snow", bg="maroon", command=validacion_de_login1)
    buton_ini.place(width=180, height=25, x=35, y=180)

    boton_close = tk.Button(vn3, text="Cerrar ventana", font=(
        "segoe ui black", 8), fg="grey1", bg="gold", command=des3)
    boton_close.place(width=180, height=20, x=35, y=260)
    vn3.resizable(0, 0)
    vn3.protocol("WM_DELETE_WINDOW", des3)
    vn3.mainloop()

# *********************************MENU DEL EMPLEADO PARA REGISTRARSE************************************************


def registrar():

    try:
        ven.withdraw()
        vn3.withdraw()
        vent_emp.withdraw()
        cl.withdraw()
    except Exception:
        pass

    global ventana_registro
    ventana_registro = tk.Toplevel(ven)
    ventana_registro.title("Registro de empleado")
    ventana_registro.geometry("500x350")

    ventana_registro.iconbitmap(
        "EXAMEN_UNIDAD3_JUANORTIZ_RAULDURAN/favicon.ico")

    img2 = PhotoImage(file="EXAMEN_UNIDAD3_JUANORTIZ_RAULDURAN/IMG2.gif")
    Label(ventana_registro, image=img2).pack()

    global user_entry
    global contra_entry

    user_entry = StringVar()
    contra_entry = StringVar()

    user_valid=StringVar()
    contra_valid=StringVar()

    user_entry = Entry(ventana_registro, validate="key", validatecommand=(ventana_registro.register(validate_entry2), "%S", "%P"), textvariable=user_valid, fg="gray78", justify="center")
    user_entry.insert(0, 'Usuario')
    user_entry.bind("<FocusIn>", bg_user2)
    user_entry.bind("<FocusOut>", bg_user2)
    user_entry.place(x=35, y=100, width=180, height=25)
    contra_entry = Entry(ventana_registro, validate="key", validatecommand=(ventana_registro.register(validate_entry), "%S", "%P"), textvariable=contra_valid, fg="gray78", justify="center")
    contra_entry.insert(0, 'Contraseña')
    contra_entry.bind("<FocusIn>", bg_contra2)
    contra_entry.bind("<FocusOut>", bg_contra2)
    contra_entry.place(x=35, y=140, width=180, height=25)

    Label(ventana_registro, bg="ghost white", text="Registrate", font=(
        "Segoe ui black", 16), fg="maroon").place(x=70, y=50)

    boton_registrar = Button(ventana_registro, text="REGISTRARSE", font=("segoe ui black", 8),
                       fg="snow", bg="maroon",command=validacion_de_login2)
    boton_registrar.place(width=180, height=25, x=35, y=180)

    boton_close = tk.Button(ventana_registro, text="Cerrar ventana", font=(
        "segoe ui black", 8), fg="grey1", bg="gold", command=des4)
    boton_close.place(width=180, height=20, x=35, y=240)

    ventana_registro.resizable(0, 0)
    ventana_registro.protocol("WM_DELETE_WINDOW", des4)
    ventana_registro.mainloop()

# ************************VENTANA DE MENU PARA EL EMPLEADO, DONDE SE VISUALIZAN LOS PEDIDOS******************


def menu_emp():

    try:
        ventana_registro.withdraw()
        vn3.withdraw()
        ven.withdraw()
    except Exception:
        pass

    global vent_emp
    vent_emp = tk.Toplevel(ven)
    vent_emp.title("Menú para empleados y pedidos")
    vent_emp.geometry("1280x700")

    vent_emp.iconbitmap(
        "EXAMEN_UNIDAD3_JUANORTIZ_RAULDURAN/favicon.ico")
    
    global tabla_pedidos
    global lista_pedidos
    global busqueda
    global busqueda2
    
    barra_menus = tk.Menu(vent_emp)
    menu_archivo = tk.Menu(barra_menus, tearoff=0)
    ventana_menu = tk.Menu(barra_menus, tearoff=0)

    barra_menus.add_cascade(menu=menu_archivo, label="Empleados")
    menu_archivo.add_command(label="Añadir empleado", command=registrar)

    barra_menus.add_cascade(menu=ventana_menu, label="Ventana")
    ventana_menu.add_command(
        label="tamaño original (1280x700)", command=tamano)
    vent_emp.config(menu=barra_menus)
    
    #Buaqueda combobox
    busqueda2=StringVar()
    busqueda2= ttk.Combobox(vent_emp, state="readonly", values=["Pastor (Precio = 15.00$ c/u)", "Asada (Precio = 15.00$ c/u)", "Tripa (Precio = 15.00$ c/u)", "Mixto (Precio = 20.00$ c/u)", "Lengua (Precio = 20.00$ c/u)", "Suadero (Precio = 20.00$ c/u)", "Chorizo (Precio = 20.00$ c/u)"], font=("calibri light", 15))
    busqueda2.place(x=30, y=150, width=300, height=30)
    
    # CREAR LA TABLA DE PEDIDOS

    tabla_pedidos = LabelFrame(
        vent_emp, text=" LISTADO DE PRODUCTOS: ")
    tabla_pedidos.grid(row=7, column=0, padx=20, pady=25)
    tabla_pedidos.place(x=10, y=200)

    lista_pedidos = ttk.Treeview(
        tabla_pedidos, height=10, columns=("#1", "#2", "#3", "#4", "#5"))
    lista_pedidos.grid(row=7, column=0, padx=20, pady=20)

    lista_pedidos.heading("#0", text="ID", anchor=CENTER)
    lista_pedidos.heading("#1", text="Tortilla", anchor=CENTER)
    lista_pedidos.heading("#2", text="Carne", anchor=CENTER)
    lista_pedidos.heading("#3", text="Salsa", anchor=CENTER)
    lista_pedidos.heading("#4", text="Orden", anchor=CENTER)
    lista_pedidos.heading("#5", text="Complemento", anchor=CENTER)

    consultar_pedido()

    busqueda_limit=StringVar()

    busqueda=tk.Entry(vent_emp, bg="ghost white", validate="key", validatecommand=(vent_emp.register(validate_entry3), "%S", "%P"), font=("corbel light", 12), textvariable=busqueda_limit)
    busqueda.place(x=150, y=40, width=150, height=20)
    busqueda.bind("<Button-1>", lambda e: busqueda.delete(0, END))

    
    button_del = Button(
        vent_emp, text="ELIMINAR PEDIDO", width="20", height="2", bg="maroon", fg="snow", font=("segoe ui black", 10), command=eliminar_elemento)
    button_del.place(x=1000, y=20)

    button_mod = Button(
        vent_emp, text="MODIFICAR", width="20", height="2", bg="maroon", fg="snow", font=("segoe ui black", 10), command=modificar_ped)
    button_mod.place(x=1000, y=140)

    button_upt = Button(
        vent_emp, text="ACTUALIZAR", width="20", height="2", bg="maroon", fg="snow", font=("segoe ui black", 10), command=actualizar_tabla)
    button_upt.place(x=1000, y=80)

    button_search = Button(
        vent_emp, text="BUSCAR", width="15", height="1", bg="maroon", fg="snow", font=("segoe ui black", 8), command=validar_busqueda)
    button_search.place(x=30, y=40)
    
    button_search2 = Button(
        vent_emp, text="BUSCAR TIPOS DE CARNE", width="30", height="1", bg="maroon", fg="snow", font=("segoe ui black", 8), command=buscar_T)
    button_search2.place(x=30, y=100)
    
    move_up = Scrollbar(tabla_pedidos, command=lista_pedidos.yview)
    move_up.grid(row=7, column=4, sticky="nsew")
    lista_pedidos.config(yscrollcommand=move_up.set)

    vent_emp.resizable(0, 0)
    vent_emp.protocol("WM_DELETE_WINDOW", des5)
    vent_emp.mainloop()

#*******************************VENTANA PARA EDITAR LOS VALORES*******************************************

def ventana_modificar():
    global ven_modify
    ven_modify = tk.Toplevel(ven)
    ven_modify.title("Modificar pedido")
    ven_modify.geometry("500x600")

    ven_modify.iconbitmap("EXAMEN_UNIDAD3_JUANORTIZ_RAULDURAN/favicon.ico")
    
    img6 = PhotoImage(file="EXAMEN_UNIDAD3_JUANORTIZ_RAULDURAN/IMG5.gif")
    Label(ven_modify, image=img6).pack()

    global tortilla_mod
    global carne_mod
    global salsas_mod
    global cantidad_mod
    global complemento_mod


    tortilla_mod = ttk.Combobox(ven_modify, state="readonly", values=[
                            "Maíz", "Harina", "Azul"], font=("calibri light", 15))
    tortilla_mod.place(x=150, y=150, width=300, height=30)

    carne_mod = ttk.Combobox(ven_modify, state="readonly", values=[
        "Pastor (Precio = 15.00$ c/u)", "Asada (Precio = 15.00$ c/u)", "Tripa (Precio = 15.00$ c/u)", "Mixto (Precio = 20.00$ c/u)", "Lengua (Precio = 20.00$ c/u)", "Suadero (Precio = 20.00$ c/u)", "Chorizo (Precio = 20.00$ c/u)"], font=("calibri light", 15))
    carne_mod.place(x=150, y=200, width=300, height=30)

    salsas_mod = ttk.Combobox(ven_modify, state="readonly", values=[
        "Salsa Roja (Xtra Picante)", "Salsa Verde", "Salsa de Chiles Mixtos", "Salsa de Ajo", "Salsa de Tomate", "Sin salsas"], font=("calibri light", 15))
    salsas_mod.place(x=150, y=250, width=300, height=30)

    cantidad_mod = ttk.Combobox(ven_modify, state="readonly", values=[
                            "Orden Individual (2 Tacos)", "Orden de Pareja (4 Tacos)", "Orden Amigos (8 Tacos)", "Orden Familiar (16 Tacos)"], font=("calibri light", 15))
    cantidad_mod.place(x=150, y=300, width=300, height=30)

    complemento_mod = ttk.Combobox(ven_modify, state="readonly", values=[
        "Nopal", "Piña", "Aguacate", "Pimientos", "Pico de gallo", "Queso", "Sin complementos"], font=("calibri light", 15))
    complemento_mod.place(x=150, y=350, width=300, height=30)

    Label(ven_modify, text="Tortilla", fg="snow", bg="maroon", width="12",
          height="2", font=("segoe ui black", 10)).place(x=30, y=144)

    Label(ven_modify, text="Carne", fg="snow", bg="maroon", width="12",
          height="2", font=("segoe ui black", 10)).place(x=30, y=194)

    Label(ven_modify, text="Salsas", fg="snow", bg="maroon", width="12",
          height="2", font=("segoe ui black", 10)).place(x=30, y=244)

    Label(ven_modify, text="Cantidad", fg="snow", bg="maroon", width="12",
          height="2", font=("segoe ui black", 10)).place(x=30, y=294)

    Label(ven_modify, text="Complementos", fg="snow", bg="maroon", width="12",
          height="2", font=("segoe ui black", 10)).place(x=30, y=344)
    
    
    tortilla_mod.set(lista_pedidos.item(lista_pedidos.selection())['values'][0])
    carne_mod.set(lista_pedidos.item(lista_pedidos.selection())['values'][1])
    salsas_mod.set(lista_pedidos.item(lista_pedidos.selection())['values'][2])
    cantidad_mod.set(lista_pedidos.item(lista_pedidos.selection())['values'][3])
    complemento_mod.set(lista_pedidos.item(lista_pedidos.selection())['values'][4])

    button_pedir = tk.Button(
        ven_modify, text="Modificar pedido", command=validar2, fg="snow", font= ("segoe ui black", 8), bg= "maroon")
    button_pedir.place(x=205, y=425, width=200, height=30)

    ven_modify.resizable(0, 0)
    ven_modify.mainloop()

# **********************************FUNCIONES PARA LA VENTANA DEL MENU************************************

def tamano():
    vent_emp.geometry("1280x700")

venp()
