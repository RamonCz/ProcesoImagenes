
import PIL.Image
from numpy import true_divide

ASCII_CHARS = ['M','N','H','#','Q','U','A','D','0','Y','2','$','%','+','.']

#ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]


def to_greyscale(image):
    return image.convert("L")

def pixel_to_ascii(image):
    pixels = image.getdata()
    print(pixels)
    ascii_str = ""
    b = True
    for pixel in pixels:
        if b:
           
            ascii_str += ASCII_CHARS[pixel//25]
    return ascii_str


def main():
    path = r'C:\Users\monch\Documents\Semestre\ProcesoImagenes\Tarea3\spider.png'
    
    
    image = PIL.Image.open(path)
    
    #print(path, "Unable to find image ")
    #resize image
    w,h = image.size
    image = image.resize((w//3,h//3), PIL.Image.ANTIALIAS)
    #convert image to greyscale image"C:\Users\monch\Documents\Semestre\ProcesoImagenes\Tarea2\spider.png"
    greyscale_image = to_greyscale(image)
    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(greyscale_image)
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img=""
    #Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    #save the string to a file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img);
main()
