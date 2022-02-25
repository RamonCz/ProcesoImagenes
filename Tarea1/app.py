from tkinter import filedialog
from filtros import color, gray1,contraste,inverso,brillo, mosaico
#from gui import gris


def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename


def gris_aux(f,name):
    if "(R*1 + G*1 + B*1) / 3 (división entera)" == f:
        gray1(1,name)
    if "(Red * 0.3 + Green * 0.59 + Blue * 0.11)" == f:
        gray1(2,name)
    if "(Red * 0.2126 + Green * 0.7152 + Blue * 0.0722)" == f:
        gray1(3,name)
    if "(Red * 0.299 + Green * 0.587 + Blue * 0.114)" == f:
        gray1(4,name)
    if "( Max(Red, Green, Blue) + Min(Red, Green, Blue) ) / 2" == f:
        gray1(5,name)
    if "Max(Red, Green, Blue)":
        gray1(6,name)
    if "Min(Red, Green, Blue)":
        gray1(7,name)


#if __name__ == '__main__': #pruebas rapidas
    # gray1(3, "spider.png")
    #color('blue','spider.png')
   # contraste('spider.png')
   # mosaico('C:/Users/monch/Documents/Semestre/ProcesoImagenes/Tarea1/spider.png',10)
    #inverso('spider.png')
    #brillo('spider.png',50)