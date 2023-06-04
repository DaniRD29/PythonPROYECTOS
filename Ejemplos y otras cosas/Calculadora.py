from customtkinter import CTk, CTkButton, CTkEntry
from tkinter import StringVar
import customtkinter as tc

class CircleButton(CTkButton):
    def __init__(self, master=None, text='',command=None):
        super().__init__(master=master, text=text, command=command)
        self.configure(width=50, heigth=70, corner_radius=20,
                       hover__color=('#cccccc', '#333333'),
                       fg_color=('#7f5af0', '#7f5af0'),
                       text_font=('Arial',16))
        self.grid(padx=5,pady=5,sticky='nsew')
        
"""def toggle_mode():
    global mode
    if mode=='ligth':
        mode='Dark'
        #ct.set_appearence_mode("Dark")
        ven.config(bg='black')
    else:
        mode='dark'
        #ct.set_appearence_mode('Ligth')
        ven.config(bg='white')"""
    
ven=CTk()
ven.config(bg="black")
ven.geometry("375x500")
ven.resizable(0,0)
#ct.set_appearece_mode("Dark")

mode='Dark'
expression=StringVar()

button_mode=CTkButton(ven,text='',
                      hover_color=('white', 'black'),
                      bg_color=('white', 'black'), width=50, heigth=50,
                      command=toggle_mode)
button_mode.grid(row=0,column=0)

entry=CTkEntry(ven,textvariable=expression,
               text_font=('Helvetica',28), justify='right', 
               text_color=('black','white'),
               corner_radius=0, state='disable',
               width=280, fg_color=('white','black'), border=0)
entry.grid(row=0, column=1, columnspan=3, padx=5, ipady=15, pady=10)

CircleButton(ven,text='C',).grid(row=1,column=0)
CircleButton(ven,text='+/-',).grid(row=1,column=1)
CircleButton(ven,text='%',).grid(row=1,column=2)
CircleButton(ven,text='÷ ',).grid(row=1,column=3)

CircleButton(ven,text='7',).grid(row=2,column=0)
CircleButton(ven,text='8',).grid(row=2,column=1)
CircleButton(ven,text='9',).grid(row=2,column=2)
CircleButton(ven,text='x',).grid(row=2,column=3)

CircleButton(ven,text='4',).grid(row=3,column=0)
CircleButton(ven,text='5',).grid(row=3,column=1)
CircleButton(ven,text='6',).grid(row=3,column=2)
CircleButton(ven,text='-',).grid(row=3,column=3)

CircleButton(ven,text='1',).grid(row=4,column=0)
CircleButton(ven,text='2',).grid(row=4,column=1)
CircleButton(ven,text='3',).grid(row=4,column=2)
CircleButton(ven,text='+',).grid(row=4,column=3)

CircleButton(ven,text='0',).grid(row=5,column=0)
CircleButton(ven,text='.',).grid(row=5,column=1)
CircleButton(ven,text='AC',).grid(row=5,column=2)
CircleButton(ven,text='=',).grid(row=5,column=3)


ven.mainloop()