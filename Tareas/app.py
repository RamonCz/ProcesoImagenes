from tkinter import filedialog
from tarea1 import gray1

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename




def gris_aux(f,name):
    if 0 == f:
        gray1(1,name)
    if 1 == f:
        gray1(2,name)
    if 2 == f:
        gray1(3,name)
    if 3 == f:
        gray1(4,name)
    if 4== f:
        gray1(5,name)
    if 5 ==f:
        gray1(6,name)
    if 6 ==f:
        gray1(7,name)


#if __name__ == '__main__': #pruebas rapidas
    # gray1(3, "spider.png")
    #color('blue','spider.png')
   # contraste('spider.png')
   # mosaico('C:/Users/monch/Documents/Semestre/ProcesoImagenes/Tarea1/spider.png',10)
    #inverso('spider.png')
    #brillo('spider.png',50)