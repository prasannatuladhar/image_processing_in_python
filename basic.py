from PIL import Image

# open the image
my_image = Image.open('image.jpg')


# check format
print(my_image.format)

# check size (something by something)
print(my_image.size)

# check mode RGB or CMYK
print(my_image.mode)

# opening and showing image
my_image.show()