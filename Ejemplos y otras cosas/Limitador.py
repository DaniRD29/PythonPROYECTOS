from tkinter import *
from tkinter import ttk

gui = Tk()
gui.geometry("200x200+50+50") 

zona_c = Canvas(gui, width = 200, height = 200) 
zona_c.config(background="cyan4")
zona_c.pack()

entry_text = StringVar() 
entry_widget = Entry(zona_c, width = 20, textvariable = entry_text,justify=CENTER) 
zona_c.create_window(100, 100, window = entry_widget)

def limitador(entry_text):
    if len(entry_text.get()) > 0:
        #donde esta el :5 limitas la cantidad d caracteres
        entry_text.set(entry_text.get()[:5])

entry_text.trace("w", lambda *args: limitador(entry_text))
gui.mainloop()