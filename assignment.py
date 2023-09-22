# Importing Image and ImageDraw from PIL
from PIL import Image, ImageDraw, ImageFont

# Adding custom font
font = ImageFont.truetype(font='static/Montserrat-Regular.ttf', size=80)
Whitefont = ImageFont.truetype(font='static/Montserrat-Light.ttf', size=28)

# Creating a template to be used
img = Image.new("RGB", (1080,1080), (0,0,0))

# Opening the image to be used
image1 = Image.open("cropped_image.jpg")

# Creating a Draw object
draw = ImageDraw.Draw(img)

# Drawing a bottom white rectangle
draw.rectangle(((0, 852), (1080, 1080)),fill = (255, 255, 255))
draw.text((90, 915), "Hairstyling In Houston", fill=(75, 71, 68), font=font)

# Drawing a pink rectangle
draw.rectangle(((0, 780), (431, 851)),fill = (223, 202, 209))
draw.text((60, 800), "Oops Upside Yo Head", fill=(255, 251, 255), font=Whitefont)

# Drawing a brown rectangle
draw.rectangle(((432, 780), (1080, 851)),fill = (43, 30, 22))

# Drawing a white rectangle
draw.rectangle(((0, 400), (101, 780)),fill = (255, 255, 255))

# Drawing a light grey rectangle
draw.rectangle(((0, 0), (101, 400)),fill = (244, 244, 246))
draw.rectangle(((100, 0), (1080, 49)),fill = (244, 244, 246))

# Pasting the cropped image
img.paste(image1, (102, 50))

# Method to save the modified image
img.save("output.jpg")
