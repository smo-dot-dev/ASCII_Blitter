import tdl
import random
from PIL import Image

FONTSIZE = 8
tdl.setFont('consolas8x8.png', 32, None, True, True, True)  # Configure the font.

# blits image to ASCII recreation of same size
def blit(fname):
    #image open
    try:
        img = Image.open(fname)
    except:
        input('ERROR: File not found.')
        return
    #image resize
    size = (W, H) = img.size
    w_blit = W // FONTSIZE
    h_blit = H // FONTSIZE
    size_blit = (w_blit, h_blit)
    img.thumbnail(size_blit, Image.ANTIALIAS)

    pix = img.load()
    #tdl renderer start
    console = tdl.init(w_blit, h_blit, 'ASCII BLITTER                               Press ANY key to save to file.')
    console.clear()
    for x in range(w_blit):
        for y in range(h_blit):
            m = (pix[x, y][0] + pix[x, y][1] + pix[x, y][2]) // 3
            if m < 9:
                c = '.'
            elif m < 22:
                c = ','
            elif m < 27:
                c = '`'
            elif m < 32:
                c = '-'
            elif m < 37:
                c = '+'
            elif m < 45:
                c = '/'
            elif m < 130:
                c = chr(random.randint(97, 120))
            elif m < 195:
                c = chr(random.randint(65, 90))
            else:
                c = str(random.randint(0, 9))
            console.draw_char(x, y, c, pix[x, y], (0, 0, 0))

    tdl.flush()
    tdl.event.key_wait()
    tdl.flush()
    tdl.screenshot()
    del console
    return

fname = input('Filename of image? ')
blit(fname)