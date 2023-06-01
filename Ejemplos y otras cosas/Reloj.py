from tkinter import Label, Tk
import time

ven=Tk()
ven.config(bg='gray')
ven.geometry('500x200')
ven.wm_attributes('-transparentcolor', 'gray')
ven.overrideredirect(1) #Eiminacion de borde de la ventana

def salir(*args):
    ven.destroy()
    ven.quit()

def get_time():
    hour=time.strftime('%H:%M:%S')
    zone=time.strftime('%Z')
    date_format=time.strftime('%A' ' ' '%d' ' ' '%B' ' ' '%Y')
    
    text_hour['text']=hour
    text_format['text']=date_format
    zone_time['text']=zone
    text_hour.after(1000, get_time)

def start(event):
    global x, y
    x=event.x
    y=event.y

def stop(event):
    global x, y
    x=None
    y=None

def move(event):
    global x, y
    deltax=event.x - x
    deltay=event.y - y
    ven.geometry("+%s+%s" %(ven.winfo_x() + deltax, ven.winfo_y() + deltay))
    ven.update

ven.bind("<ButtonPress-1>", start)#Monitorear la función de respuesta de operación de presionar boton izquierdo
ven.bind("<ButtonRelease-1>", stop)#Monitorea la función de respuesta de respuesta de operacion de liberacion del boton izquierdo
ven.bind("<B1-Motion>", move)#Función de respuesta del movimiento del mouse del monitor
ven.bind("<KeyPress-Escape>", salir)

text_hour=Label(ven, fg='white', bg='gray', font=('Star Jedi Hollow', 50, 'bold'), width=10)
text_hour.grid(column=0, row=0, ipadx=1, ipady=1)

text_format=Label(ven, fg='white', bg='gray', font=('Vivaldi', 20, 'bold'))
text_format.grid(column=0, row=1)

zone_time=Label(ven, fg='white', bg='gray', font=('Lucida Sans',12))
zone_time.grid(column=0, row=1)

get_time()
ven.mainloop()


