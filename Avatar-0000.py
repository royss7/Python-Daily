# Python Daily 0000
# June 18th, 2015
# To add a digit nubmer like 2 on the top right of your avatar of QQ
# liuyy

from PIL import Image, ImageDraw, ImageFont

if __name__ == '__main__':
    import sys
    try:
        p = Image.open(sys.argv[1])
        draw = ImageDraw.Draw(p)
        width, height = p.size
        myfont = ImageFont.load_default()
        draw.text((width/8*7, height / 10), "7", fill = 'red', font = myfont)
        #p.show(title = 'Head Picture')
        p.save("changed.jpg", "jpeg")
    except FileNotFoundError:
        print("error")

