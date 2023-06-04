#Funciones de crud
import sqlite3
    
class Comunicate():
    def __init__(self):
        self.conexion=sqlite3.connect('datas')
    
    def insert_d(self, nombre, edad, correo, telefono):
        cursor=self.conexion.cursor()
        bd="INSERT INTO table_d (NOMBRE, EDAD, CORREO, TELEFONO) VALUES ('{}', '{}','{}', '{}')"
        datos=(nombre, edad, correo, telefono)
        cursor.execute(bd,datos)
        self. conexion.commit()
        cursor.close()
    
    def mostrar_d(self):
        cursor=self.conexion.cursor()
        bd="SELECT * FROM table_d"
        cursor.execute(bd)
        datos= cursor.fetchall()
        return datos
    
    def delete_d(self,nombre):
        cursor=self.conexion.cursor()
        bd='''DELETE FROM table_d WHERE NOMBRE = '{}' '''.format(nombre)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
        
    def actualizar_d(self, ID, nombre, edad, correo, telefono):
        cursor=self.conexio.cursor()
        bd='''UPDATE table_d SET NOMBRE = '{}', EDAD = '{}', CORREO = '{}', TELEFONO = '{}'
        WHERE ID = '{}' '''.format(nombre, edad, correo, telefono, ID)
        cursor.execute(bd)
        dato=cursor.rowcount()
        self.conexion.commit()
        cursor.close()
        return dato
        