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

# rotate image
my_image = Image.open('image.jpg')
after_rotate = my_image.rotate(180)
after_rotate.save("rotated.png","png")

# resize image -must pass in tuple if not does not work
my_image = Image.open('image.jpg')
after_resize = my_image.resize((200,200),)
after_resize.save("resized.png","png")

# Thumbnail - Resize without squizing the image with good aspect ratio
my_image = Image.open('bnw.jpg')
my_image.thumbnail((400,400),) #must pass in tuple in oder to work
my_image.save('thumbnai.png')


# Crop -copying a sub rectangle from image
my_image = Image.open('image.jpg')
box = (200,200,400,400)
after_crop = my_image.crop(box)
after_crop.save("cropped.png","png")

