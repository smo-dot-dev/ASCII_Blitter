from PIL import Image
DOWNSCALE_FACTOR = 10
image_path = "Untitled.png"
paleta = "@$#smodotdev;=~+-*,."

RGB_AS_BACKGROUND = False
FORCE_SQUARE = True

# Para mapear del 0-255 a 0-len(paleta), devuelve int
def remap(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

# Se pasa un objeto Image y se hace un resize al tamaño dividido entre DOWNSCALE_FACTOR
def resize(img, font_size):
    img_width, img_height = img.size
    thumbnail_width = img_width // font_size
    thumbnail_height = img_height // font_size
    img.thumbnail((thumbnail_width, thumbnail_height))
    return img

#image open
img = Image.open(image_path)
#image resize
img = resize(img, DOWNSCALE_FACTOR)

#pix is 2d array of (int,int,int)
pix = img.load()
html_text = ""
#html style: set 8x8 font
html_text += "<style>body{font-family:monospace;font-size:10px;}</style>"
output_console = ""
print("Image size: {}x{}".format(img.size[0], img.size[1]))

if not RGB_AS_BACKGROUND:
    paleta = paleta[::-1]

for j in range(img.size[1]):
    for i in range(img.size[0]):
        # m es el promedio de los 3 canales de color, se usa para mapear a la paleta
        m = (pix[i, j][0] + pix[i, j][1] + pix[i, j][2])//3
        char = paleta[remap(m,0,255,0,len(paleta)-1)]
        output_console += char
        #print("rgb({},{},{})".format(pix[i, j][0], pix[i, j][1], pix[i, j][2]))
        #generate HTML with rgb as text color, black background, monospaced font, using paleta[remap(m,0,255,0,len(paleta)-1)] as text
        rgb_colors = "rgb({},{},{})".format(pix[i, j][0], pix[i, j][1], pix[i, j][2])

        if RGB_AS_BACKGROUND:
            char_to_html = "<span style=\"color:black;background-color:{};font-family:monospace;\">{}</span>".format(rgb_colors, char)
        else:
            char_to_html = "<span style=\"color:{};background-color:white;font-family:monospace;\">{}</span>".format(rgb_colors, char)

        html_text += char_to_html
        if FORCE_SQUARE:
            output_console += char
            html_text += char_to_html


    output_console+='\n'
    html_text += "<br>"



#output html to file
with open("output.html", "w") as f:
    f.write(html_text)

print(output_console)
print("Output with colors saved to output.html")