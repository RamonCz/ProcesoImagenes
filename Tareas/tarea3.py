from matplotlib.pyplot import gray
from tarea1 import mosaico, gray1
from PIL import Image,ImageDraw,ImageFont


def image_letters(name, letter = "M", gray = False):
    cour_font = ImageFont.truetype("cour.ttf", 18, encoding="unic")
    input_image = Image.open(name)
    if gray:# tranforms image to gray with myfunction
        input_image = gray1(1,name)
    x,y = 0,4
    arr = mosaico(input_image,5,True)
   
    w,h = arr.shape

    # get the line size
    text_width, text_height = cour_font.getsize(letter)

    # create a blank canvas with extra space between lines
    canvas = Image.new('RGB', ((text_width+x)*w , (text_height-y)*h), (255, 255, 255)) # +w+h
    draw = ImageDraw.Draw(canvas)
    for i in range(w):
        for j in range(h):        
            # draw the text onto the textcanvas, and use black as the text color
            color = arr[i][j]
            draw.text((i*(text_width+x),j*(text_height-y)), letter, font = cour_font, fill = color)


    # save the blank canvas to a file
    #canvas.show()
    canvas.save("unicode-text.png", "PNG")


image_letters(r'C:\Users\monch\Documents\Semestre\ProcesoImagenes\Tarea3\spider.png',gray= True)