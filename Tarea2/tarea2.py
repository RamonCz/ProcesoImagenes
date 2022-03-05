from telnetlib import SEND_URL
from tkinter import *
from PIL import Image
import numpy as np

class kernel:

    def __init__(self, nombre,array, factor, bias) -> None:
        self.nombre = nombre
        self.array = array
        self.factor = factor
        self.bias = bias

def blur(nombre):
    blur = np.array([[0.0, 0.2,  0.0,],
                        [0.2, 0.2,  0.2,],
                        [0.0, 0.2,  0.0]])
    
    factor =  1.0
    bias = 0.0
    input_image = Image.open(nombre)
    convolve(input_image, blur,factor,bias)

def motion_blur(nombre):
    motion_blur = np.array([
                        [1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1]])

    factor =  1.0 / 9.0
    bias = 0.0
    input_image = Image.open(nombre)
    convolve(input_image, motion_blur,factor,bias)
    
def find_edges(nombre,ker):
    horizontal  = kernel('horizontal ', np.array([
                                    [0,  0, -1,  0,  0],
                                    [0,  0, -1,  0,  0],
                                    [0,  0,  2,  0,  0],
                                    [0,  0,  0,  0,  0],
                                    [0,  0,  0,  0,  0]]), 1.0, 0.0)
    vertical = kernel('vertical', np.array([
                                    [0,  0, -1,  0,  0],
                                    [0,  0, -1,  0,  0],
                                    [0,  0,  4,  0,  0],
                                    [0,  0, -1,  0,  0],
                                    [0,  0, -1,  0,  0]]), 1.0, 0.0)
    degrees45 = kernel('45', np.array([
                                    [-1,  0,  0,  0,  0],
                                    [0, -2,  0,  0,  0],
                                    [0,  0,  6,  0,  0],
                                    [0,  0,  0, -2,  0],
                                    [0,  0,  0,  0, -1]]), 1.0, 0.0)
    all_directions = kernel('all directions', np.array([
                                    [-1, -1, -1],
                                    [-1,  8, -1],
                                    [-1, -1, -1]]), 1.0, 0.0)
    dic = {'horizontal':horizontal, 'vertical':vertical, 'degrees45':degrees45, 'all_directions':all_directions}
    input_image = Image.open(nombre)
    convolve(input_image, dic[ker].array,dic[ker].factor,dic[ker].bias)
    
   
def sharpen(nombre):
    sharpen1 = np.array([
                            [-1, -1, -1],
                            [-1,  9, -1],
                            [-1, -1, -1]])

    factor =  1.0 
    bias = 0.0
    input_image = Image.open(nombre)
    convolve(input_image, sharpen1,factor,bias)

def emboss(nombre):
    emboss1 = np.array([
                        [-1, -1,  0],
                        [-1,  0,  1],
                        [0,  1,  1]])

    factor =  1.0 
    bias = 128.0
    input_image = Image.open(nombre)
    convolve(input_image, emboss1,factor,bias)

def mean(nombre):
    mean1 = np.array([
                    [1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]])

    factor =  1.0/9.0 
    bias = 0.0
    input_image = Image.open(nombre)
    convolve(input_image, mean1,factor,bias)

def median(nombre):
    median1 = np.array([
                    [1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]])

    factor =  1.0
    bias = 0.0
    input_image = Image.open(nombre)
    convolve(input_image, median1,factor,bias)

def conv_filter(filter):
    f = np.dstack((filter,filter))
    f = np.dstack((f,filter)) 
    return f

def convolve(img, kernel, factor, bias):
    '''
    Aplica la convolucion a una matriz nxm
    '''
    k = kernel.shape[0]
    
    w , h = img.size
    img = img.resize((w//3,h//3), Image.ANTIALIAS)
    w , h = img.size
    pixel_map = img.load()
    #w,h = calculate_target_size(img.size,kernel)
    # Iterate over the rows
    for i in range(w):
        # Iterate over the columns
        for j in range(h):
            r = 0 
            g = 0
            b = 0
            if ((i+k) < w and (j+k) < h):
                #print(i+k,j+k)
                i3 = 0
                for i2 in range(i,i+k): 
                    j3 = 0
                    for j2 in range(j,j+k):
                        #imageX = (i - tgt_size[0]  / 2 + filterX + w) % w
                        #imageY = (j - tgt_size[1] / 2 + filterY + h) % h
                        r2, g2, b2 = img.getpixel((i2, j2))
                        r += r2 * kernel[i3,j3]
                        g += g2 * kernel[i3,j3]
                        b += b2 * kernel[i3,j3]
                        j3 +=1
                    i3 +=1
                        
            r = min(max(int(factor * r + bias), 0), 255)
            g = min(max(int(factor * g + bias), 0), 255)
            b = min(max(int(factor * b + bias), 0), 255) 

            pixel_map[i,j] = (r,g,b)
    img.show()       