from tkinter import Tk, Button, Entry, Label, ttk
from tkinter import *
from tkinter import StringVar, messagebox
from CRUDMEJORADO import Comunicate
from time import strftime
import pandas as pd

class Ven(Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.nombre=StringVar()
        self.edad=StringVar()
        self.correo=StringVar()
        self.telefono=StringVar()
        
        self.master.columnconfigure(0,weight=1)
        self.master.rowconfigure(0,weight=1)
        self.master.rowconfigure(1,weight=5)
        self.datas=Comunicate()
        
        self.widgets()
    
    def widgets(self):
        self.frm_uno=Frame(self.master, background='white', height=200, width=800)
        self.frm_uno.grid(column=0, row=0, sticky='nsew')
        self.frm_dos=Frame(self.master, bg='white', height=300, width=800)
        self.frm_dos.grid(column=0, row=1, sticky='nsew')
        
        self.frm_uno.columnconfigure([0,1,2], weight=1)
        self.frm_uno.rowconfigure([0,1,2,3,4,5],weight=1)
        self.frm_dos.columnconfigure(0, weight=1)
        self.frm_dos.rowconfigure(0,weight=1)
        
        Label(self.frm_uno, text='Opciones', bg='white', fg='black', 
              font=('Kaufmann BT',13, 'bold')).grid(column=2,row=0)
        Button(self.frm_uno, text='Refrescar', font=('Arial', 9,'bold'),command=self.actualizar_d,
               fg='black', bg='deep sky blue', width=20, bd=3). grid(column=2, row=1, pady=5)
        
        Label(self.frm_uno, text='Agregar y actualizar datos', bg='white', fg='black', 
              font=('Kaufmann BT',13, 'bold')).grid(columnspan=2, column=0, row=0, pady=5)
        Label(self.frm_uno, text='Nombre', bg='white', fg='black', 
              font=('Rockwell',13, 'bold')).grid(column=0, row=1, pady=5)
        Label(self.frm_uno, text='Edad', bg='white', fg='black', 
              font=('Rockwell',13, 'bold')).grid(column=0, row=2, pady=5)
        Label(self.frm_uno, text='Correo', bg='white', fg='black', 
              font=('Rockwell',13, 'bold')).grid(column=0, row=3, pady=5)
        Label(self.frm_uno, text='Telefono', bg='white', fg='black', 
              font=('Rockwell',13, 'bold')).grid(column=0, row=4, pady=5)
        
        Entry(self.frm_uno,textvariable=self.nombre, font=('Comic Sans MS', 12),
              highlightbackground= "deep sky blue", highlightthickness=5).grid(column=1,row=1)
        Entry(self.frm_uno,textvariable=self.edad, font=('Comic Sans MS', 12),
              highlightbackground= "deep sky blue", highlightthickness=5).grid(column=1,row=2)
        Entry(self.frm_uno,textvariable=self.correo, font=('Comic Sans MS', 12),
              highlightbackground= "deep sky blue", highlightthickness=5).grid(column=1,row=3)
        Entry(self.frm_uno,textvariable=self.telefono, font=('Comic Sans MS', 12),
              highlightbackground= "deep sky blue", highlightthickness=5).grid(column=1,row=4)
        
        Button(self.frm_uno, text="AÑADIR DATOS", font=('Arial',9, 'bold'), bg='deep sky blue', 
               width=20, bd=3, command=self.agregar_d).grid(column=2, row=2, padx=5, pady=5)
        Button(self.frm_uno, text="LIMPIAR CAMPOS", font=('Arial',9, 'bold'), bg='deep sky blue', 
               width=20, bd=3, command=self.clear_campos).grid(column=2, row=3, padx=5, pady=5)
        Button(self.frm_uno, text="ACTUALIZAR DATOS", font=('Arial',9, 'bold'), bg='deep sky blue', 
               width=20, bd=3, command=self.actualizar_t).grid(column=2, row=4, padx=5, pady=5)
        Button(self.frm_uno, text="EXPORTAR A EXCEL", font=('Arial',9, 'bold'), bg='deep sky blue', 
               width=20, bd=3, command=self.guardar_d).grid(column=2, row=5, padx=5, pady=5)
        
        style_t= ttk.Style()
        style_t.configure("Treeview", font=("Helvetica", 10, 'bold'), foreground='black',
                          background='white')
        style_t.map("Treeview", background=[('selected', "deep sky blue")], foreground=[('selected', "black")])
        style_t.configure('Heading', background='white', foreground="deep sky blue", padding=3,
                          font=('Arial',10, 'bold'))
        
        self.tabla= ttk.Treeview(self.frm_dos)
        self.tabla.grid(column=0, row=0, sticky='nsew')
        ladox=ttk.Scrollbar(self.frm_dos, orient='horizontal', command=self.tabla.xview)
        ladox.grid(column=0, row=1, sticky='ew')
        ladoy=ttk.Scrollbar(self.frm_dos, orient='vertical', command=self.tabla.yview)
        ladoy.grid(column=1, row=0, sticky='ns')
        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)
        
        self.tabla['columns']=('Edad', 'Correo','Telefono')
        self.tabla.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla.column('Edad', minwidth=100, width=120, anchor='center')
        self.tabla.column('Correo', minwidth=100, width=120, anchor='center')
        self.tabla.column('Telefono', minwidth=100, width=105, anchor='center')
        
        self.tabla.heading('#0', text='Nombre', anchor='center')
        self.tabla.heading('Edad', text='Edad', anchor='center')
        self.tabla.heading('Correo', text='Correo', anchor='center')
        self.tabla.heading('Telefono', text='Telefono',anchor='center')
        
        self.tabla.bind("<<TreeviewSelect>>", self.get_r)
        self.tabla.bind("<Double-1>", self.delete_dat)
    
    #Obtener filas
    def get_r(self, event):
        item=self.tabla.focus()
        self.table_d= self.tabla.item(item)
        self.nombre.set(self.table_d['text'])
        self.edad.set(self.table_d['values'][0])
        self.correo.set(self.table_d['values'][1])
        self.telefono.set(self.table_d['values'][2])
        
    def delete_dat(self, event):
        self.clear_campos()
        item=self.tabla.selection()[0]
        x=messagebox.askquestion('Informacion', '¿Desea eliminar?')
        if x== 'yes':
            self.tabla.delete(item)
        self.datas.delet_d(self.table_d['text'])
    
    def agregar_d(self):
        nombre= self.nombre.get()
        edad=self.edad.get()
        correo=self.correo.get()
        telefono=self.telefono.get()
        datos=(edad, correo, telefono)
        if nombre and edad and correo and telefono !="":
            self.tabla.insert('',0, text="nombre", values = datos)     
            self.datas.insert_d(nombre, edad, correo, telefono )
            self.clear_campos()
            
    def actualizar_t(self):
        self.clear_campos()
        datos=self.datas.mostrar_d()
        self.tabla.delete(*self.tabla.get_children())
        i=-1
        for dato in datos:
            i=i+1
            self.tabla.insert('', i, text=datos[i][1:2][0], values=datos[i][2:5])
            
    def actualizar_d(self):
        item=self.tabla.focus()
        self.table_d= self.tabla.item(item)
        nombre=self.table_d['text']
        datos=self.datas.mostrar_d()
        for fila in datos:
            Id= fila[0]
            nombre_bd=fila[1]
            if nombre_bd == nombre:    
                if Id !=None:
                    nombre=self.nombre.get()
                    edad=self.edad.get()
                    correo=self.correo.get()
                    telefono=self.telefono.get()
                    if nombre and edad and correo and telefono !="":
                        self.datas.actualizar_d(Id, nombre, edad, correo, telefono)
                        self.tabla.delete(*self.tabla.get_children())
                        i=-1
                        for dato in datos:
                            i=i+1
                            self.tabla.insert('',i, text=datos[i][1:2][0], values=datos[i][2:5])
    
    
    #Limpiar campos                
    def clear_campos(self):        
        self.nombre.set('')
        self.edad.set('')
        self.correo.set('')
        self.telefono.set('')
        
    def guardar_d(self):
        datos=self.table_d.mostrar_d()   
        i=-1
        nombre, edad, correo, telefono=[], [], [],[]
        for dato in datos:
            i=i+1
            nombre.append([i][1])
            edad.append([i][2])
            correo.append([i][3])
            telefono.append([i][4])
        fecha=str(strftime('%d-%m-%y_%H-%M-%S'))
        datos={'Nombres':nombre, 'Edad':edad, 'Correo':correo, 'Telefono':telefono}
        df=pd.DataFrame(datos, columns=['Nombre','Edad', 'Correo', 'Telefono'])
        df.to_excel((f'Datos',{fecha}.xlsx))
          
if __name__=="__main__":
    vent = Tk()
    vent.title('')
    vent.minsize(height=400, width=600)
    vent.geometry('800x500')
    app=Ven(vent)
    app.mainloop()     