from PIL import Image,ImageOps
from numpy import array, append,expand_dims,empty

def gray1(number, nombre):
    '''
    Convierte una imagen a escala de grises
    '''
    if(nombre != None):
        input_image = Image.open(nombre)
        pixel_map = input_image.load()
        w, h = input_image.size
        for i in range(w):
            for j in range(h):
                r, g, b = input_image.getpixel((i, j))
                grayscale = 1
                if (number == 1):
                    grayscale = (r + g + b)//3
                elif (number < 5):
                    r1 = 1
                    g1 = 1
                    b1 = 1
                    if(number == 2):
                        r1 = 0.3
                        g1 = 0.59
                        b1 = 0.11
                    elif (number == 3):
                        r1 = 0.2126
                        g1 = 0.7152
                        b1 = 0.0722
                    elif (number == 4):
                        r1 = 0.299
                        g1 = 0.587
                        b1 = 0.114
                    grayscale = (r1*r + g1*g + b1*b)
                else:
                    if(number == 5):
                        grayscale = (max(r,g,b) + min(r,g,b))/2
                    elif(number == 6):
                        grayscale = max(r,g,b)
                    elif(number == 7):
                        grayscale = min(r,g,b)

                
                pixel_map[i, j] = (int(grayscale), int(grayscale), int(grayscale))
        
        #input_image.save("grayscale", format="png")
        input_image.show()
        return input_image
def color(color, nombre):
    '''
    Convierte una imagen al color indicado
    '''
    if(nombre != None):
        input_image = Image.open(nombre)
        pixel_map = input_image.load()
        w, h = input_image.size
        for i in range(w):
            for j in range(h):
                r, g, b = input_image.getpixel((i, j))
                dic = {'red': (r,0,0), 'green':(0,g,0), 'blue':(0,0,b)}
                pixel_map[i, j] = dic[color]
        
        input_image.show()


def mosaico(nombre,number, letter = False):
    if(nombre == str):
        input_image = Image.open(nombre)
    else:
        input_image = nombre
    w, h = input_image.size
    
    average = _mosaico_aux(input_image, 0, 0, number,number, 0,0, flag = 0)
    
    arr = array([],dtype=object)
    prom = []
    flag = False
    for i in range(0,w,number):
        if letter and flag :
            if len(arr.shape) == 1:
                aux = empty(len(prom), dtype=object)
                aux[:] = prom
                arr = append(arr, aux)
                arr = expand_dims(arr, axis=0)
                prom = []
            else:
                aux = empty((1,len(prom)), dtype=object)
                aux[:] =  [prom]
                arr = append(arr, aux, axis=0)
                prom = []
        for j in range(0,h,number):
            flag = True
            width  = i +number
            height = j + number
            if (width  < w and height < h):
                average = _mosaico_aux(input_image, i, j, width ,height, average,number)
                prom.append(average)
            elif(width  >= w and height >= h):
                average = _mosaico_aux(input_image, i, j, w ,h, average,number)
                prom.append(average)
            elif(width  >= w):
                average = _mosaico_aux(input_image, i, j, w ,height, average,number)
                prom.append(average)
            elif(height >= h):
                average = _mosaico_aux(input_image, i, j, width ,h, average,number)
                prom.append(average)

    
    #input_image.show()
    return arr

def _mosaico_aux(input_image, x, y, w, h, average,n,flag = 1  ):
    pixel_map = input_image.load()
    w2, h2 = input_image.size
    main = []
    flag2 = False
    for i in range(x,w):
        for j in range(y,h):
            if (flag != 0 ):
                pixel_map[i, j] = average
            if(i+n < w2 and j+n < h2):
                flag2 = True
                r, g, b = input_image.getpixel((i+n, j+n))
                main.append((r/3,g/3,b/3))
    if (flag2):
        r, g, b = zip(*main)
        red = sum(r) /len(r)
        green = sum(g) /len(g)
        blue = sum(b) /len(b)
        #add the color to array
        return (int(red), int(green), int(blue))
    return (0,0,0)

def contraste(nombre):
    if(nombre != None):
        input_image = Image.open(nombre)
        pixel_map = input_image.load()
        w, h = input_image.size
        for i in range(w):
            for j in range(h):
                r, g, b = input_image.getpixel((i, j))
                red = 255 if r > 127 else 0
                green = 255 if g > 127 else 0
                blue = 255 if b > 127 else 0
                
                pixel_map[i, j] = (red,green,blue)
        
        input_image.show()

def inverso(nombre):
    if(nombre != None):
        input_image = Image.open(nombre)
        pixel_map = input_image.load()
        w, h = input_image.size
        for i in range(w):
            for j in range(h):
                r, g, b = input_image.getpixel((i, j))
                red = 255 if r < 127 else 0
                green = 255 if g < 127 else 0
                blue = 255 if b < 127 else 0
                
                pixel_map[i, j] = (red,green,blue)
        
        input_image.show()

def brillo(nombre, num):
    if(nombre != None):
        if (num > 254):
            print("Demasiado brillo")
        else:
            input_image = Image.open(nombre)
            pixel_map = input_image.load()
            w, h = input_image.size
            for i in range(w):
                for j in range(h):
                    r, g, b = input_image.getpixel((i, j))
                    
                    pixel_map[i, j] = (r+num,g+num,b+num)
            return input_image.show()