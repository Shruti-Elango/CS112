
''' Purpose: demonstrate simple drawing commands '''

from PIL import Image, ImageDraw

def picture() :

    # replace dimensions and background as you see fit
    WIDTH  = 750
    HEIGHT = 500

    DIMENSIONS = [ WIDTH, HEIGHT]

    BACKGROUND_COLOR = "LightBlue"

    # create image of appropriate size
    im = Image.new( 'RGB', DIMENSIONS, BACKGROUND_COLOR )

    # get a drawable canvas of image im
    canvas = ImageDraw.Draw( im )

    # put your drawing commands here
    p0= (0,500)
    p1= (0,349)
    p2= (750, 349)
    p3= (750,500)
    seq = [p0, p1, p2, p3]
    canvas.polygon (seq, fill= 'Tan')

    p0 = (200, 375)
    p1 = (400, 375)
    p2 = (400, 250)
    p3 = (200,250)
    seq = [p0, p1, p2, p3]
    canvas.polygon(seq, fill='Red', outline = 'Black')

    p0 = (400, 375)
    p1 = (400, 250)
    p2 = (475, 230)
    p3 = (475, 350)
    seq = [p0, p1, p2, p3]
    canvas.polygon(seq, fill='DarkRed', outline='Black')

    p0 = (200, 250)
    p1 = (400, 250)
    p2 = (300, 200)
    seq = [p0, p1, p2]
    canvas.polygon(seq, fill='DarkGrey', outline = 'Black')

    p0 = (300, 200)
    p1 = (400, 250)
    p2 = (475, 230)
    p3 = (400,180)
    seq = [p0, p1, p2, p3]
    canvas.polygon(seq, fill='Grey', outline='Black')

    p0 = (300, 375)
    p1 = (350, 375)
    p2 = (350, 300)
    p3 = (300, 300)
    seq = [p0, p1, p2, p3]
    canvas.polygon(seq, fill='White', outline='Black')

    p0 = (250, 375)
    p1 = (300, 375)
    p2 = (300, 300)
    p3 = (250, 300)
    seq = [p0, p1, p2, p3]
    canvas.polygon(seq, fill='White', outline='Black')


    x = 100
    y = 75
    w = 125
    h = 125
    xy = [(x, y), (x + w, y + h)]
    canvas.ellipse(xy, fill="Orange")

    x = 110
    y = 85
    w = 100
    h = 100
    xy = [(x, y), (x + w, y + h)]
    canvas.ellipse(xy, fill="Yellow")


    p0 = (650, 375)
    p1 = (658, 375)
    p2 = (658, 250)
    p3 = (650, 250)
    seq = [p0, p1, p2, p3]
    canvas.polygon(seq, fill='Brown')

    x= 600
    y= 200
    w=50
    h=50
    xy= [(x,y),(x+w, y+h)]
    canvas.ellipse(xy, fill="DarkGreen")

    x = 650
    y = 200
    w = 50
    h = 50
    xy = [(x, y), (x + w, y + h)]
    canvas.ellipse(xy, fill="Green")

    x = 625
    y = 215
    w = 50
    h = 50
    xy = [(x, y), (x + w, y + h)]
    canvas.ellipse(xy, fill="DarkGreen")

    x = 615
    y = 150
    w = 50
    h = 50
    xy = [(x, y), (x + w, y + h)]
    canvas.ellipse(xy, fill="Green")

    x = 620
    y = 165
    w = 50
    h = 50
    xy = [(x, y), (x + w, y + h)]
    canvas.ellipse(xy, fill="DarkGreen")

    x = 635
    y = 159
    w = 50
    h = 50
    xy = [(x, y), (x + w, y + h)]
    canvas.ellipse(xy, fill="Green")

    coord= (275, 400)
    s= "Shruti's Future Home ;)"
    canvas.text(coord, s, fill= 'Black')


    # return the art
    return im

# no changes to the below

if ( __name__ == "__main__" ) :

    im = picture()

    im.show()

    im.save( 'artistry.jpg' )
