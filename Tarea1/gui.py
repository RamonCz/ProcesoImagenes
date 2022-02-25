from lib2to3.pgen2.token import NAME
from app import openfn, gris_aux
from tkinter import *
import tkinter
from PIL import ImageTk, Image
from filtros import color, gray1,contraste,inverso,brillo, mosaico
import os

root = Tk()
root.geometry("1000x800+300+150")
root.resizable(width=True, height=True)

def filtros(namef):
    options_list = ["Gray", "Red", "Green", "Blue", "Mosaico","Alto contraste", "Inverso", "Brillo"]
    value_inside = tkinter.StringVar(root)
    value_inside.set("Select an Option")
    question_menu = tkinter.OptionMenu(root, value_inside, *options_list)
    question_menu.pack()
    print(value_inside.get())
    submit_button = tkinter.Button(root, text='Apply', command=lambda :filtro(value_inside.get(),namef))
    submit_button.pack()
    

def gris(name):
    options_list = ["(R*1 + G*1 + B*1) / 3 (división entera)",
                    "(Red * 0.3 + Green * 0.59 + Blue * 0.11)",
                    "(Red * 0.2126 + Green * 0.7152 + Blue * 0.0722)",
                    "(Red * 0.299 + Green * 0.587 + Blue * 0.114)",
                    "( Max(Red, Green, Blue) + Min(Red, Green, Blue) ) / 2",
                    "Max(Red, Green, Blue)",
                    "Min(Red, Green, Blue)"]
    value_inside = tkinter.StringVar(root)
    value_inside.set("Select an Option")
    question_menu = tkinter.OptionMenu(root, value_inside, *options_list)
    question_menu.pack()
    print(value_inside.get())
    submit_button = tkinter.Button(root, text='Apply', command=lambda :gris_aux(value_inside.get(),name))
    submit_button.pack()

def filtro(f,name):
    #dic = {"Gray":gray1(1,name), 
    if "Gray" == f:
        gris(name)
    if "Red" == f:
        color('red',name)
    if "Green" == f:
        color('green',name)
    if  "Blue" == f:
        color('blue',name)
    if  "Mosaico" ==f :
        mosaico(name,10)
    if "Alto contraste"== f:
        contraste(name)
    if "Inverso" == f:
        inverso(name)
    if "Brillo" == f:
        brillo(name,40)


def open_img():
    namef = openfn()
    img = Image.open(namef)
    img = img.resize((300, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()
    filtros(namef)

bnt = Button(root, text='Open image', command=open_img).pack()





# run the application
root.mainloop()