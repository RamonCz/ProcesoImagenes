from lib2to3.pgen2.token import NAME
from tkinter import *
import tkinter as tk
from app import gris_aux, openfn
from filtros import color,contraste,inverso,brillo, mosaico
from PIL import ImageTk, Image

root = Tk()
root.geometry("1000x800+300+150")
root.resizable(width=True, height=True)

string_var = tk.StringVar()
def open_img():
    namef = openfn()
    img = Image.open(namef)
    img = img.resize((500, 400), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()
    string_var.set(namef)

def scaling(option):
    scale = tk.Toplevel(root)
    scale.geometry("200x50") 
    v = IntVar() 
    if option == 0:
        scale = Scale( scale, variable = v, from_ = 1, to = 50, orient = HORIZONTAL,length=800,sliderlength=10,resolution=2)  
    else:
        scale = Scale( scale, variable = v, from_ = 1, to = 100, orient = HORIZONTAL,length=800,sliderlength=10,resolution=2)  
    scale.pack(anchor=CENTER) 
    btn = Button(scale, text="Value", command=lambda : escalas(scale,option,v))  
    btn.pack()  
    
    label = Label(scale)  
    label.pack()  
    
def escalas(scale,option,v):
    try:
        scale.destroy()
        scale.destroy()
    except:
        pass
    if option == 0  :
        mosaico(string_var.get(),v.get())
    if option == 1 :
        brillo(string_var.get(),v.get())

menubar = tk.Menu(root)
root.config(menu=menubar)

filemenu = tk.Menu(menubar)
filemenu.add_command(label="Open", command=open_img)
filemenu.add_command(label="Save")
filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)

filtermenu = tk.Menu(menubar)

graymenu = tk.Menu(menubar)
options_list = ["(R*1 + G*1 + B*1) / 3 (división entera)",
                    "(Red * 0.3 + Green * 0.59 + Blue * 0.11)",
                    "(Red * 0.2126 + Green * 0.7152 + Blue * 0.0722)",
                    "(Red * 0.299 + Green * 0.587 + Blue * 0.114)",
                    "( Max(Red, Green, Blue) + Min(Red, Green, Blue) ) / 2",
                    "Max(Red, Green, Blue)",
                    "Min(Red, Green, Blue)"]
graymenu.add_command(label= options_list[0],command=lambda :gris_aux(0,string_var.get()))
graymenu.add_command(label= options_list[1],command=lambda :gris_aux(1,string_var.get()))
graymenu.add_command(label= options_list[2],command=lambda :gris_aux(2,string_var.get()))
graymenu.add_command(label= options_list[3],command=lambda :gris_aux(3,string_var.get()))
graymenu.add_command(label= options_list[4],command=lambda :gris_aux(4,string_var.get()))
graymenu.add_command(label= options_list[5],command=lambda :gris_aux(5,string_var.get()))
graymenu.add_command(label= options_list[6],command=lambda :gris_aux(6,string_var.get()))


filtermenu.add_cascade(label="Gray", menu=graymenu)
filtermenu.add_command(label= "Red", command=lambda :color('red',string_var.get()))
filtermenu.add_command(label= "Green",command=lambda :color('green',string_var.get()))
filtermenu.add_command(label= "Blue",command=lambda :color('blue',string_var.get()))
filtermenu.add_command(label= "Mosaico",command=lambda :scaling(0))
filtermenu.add_command(label="Alto contraste",command=lambda :contraste(string_var.get()))
filtermenu.add_command(label= "Inverso",command= lambda :inverso(string_var.get()))
filtermenu.add_command(label= "Brillo",command= lambda: scaling(1))#  lambda :brillo(string_var.get(),40))

menubar.add_cascade(label="Filter", menu=filtermenu)



# run the application
root.mainloop()