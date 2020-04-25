from PIL import Image,ImageFilter

my_image = Image.open('image.jpg')

my_image_blur = my_image.filter(ImageFilter.BLUR)
my_image_blur.save("after_blur.png",'png')

my_image_sharpen = my_image.filter(ImageFilter.SHARPEN)
my_image_sharpen.save("after_sharpen.png",'png')

# what else can we do?
# BLUR,SHARPEN,CONTOUR,DETAIL,EDGE_ENHANCE,EDGE_ENHANCE_MORE,EMBOSS,FIND_EDGES,SMOOTH,SMOOTH_MORE

my_image_contour = my_image.filter(ImageFilter.CONTOUR)
my_image_contour.save("after_contour.png",'png')


my_image_detail = my_image.filter(ImageFilter.DETAIL)
my_image_detail.save("after_detail.png",'png')

my_image_emboss = my_image.filter(ImageFilter.EMBOSS)
my_image_emboss.save("after_emboss.png",'png')

my_image_find_edges = my_image.filter(ImageFilter.FIND_EDGES)
my_image_find_edges.save("after_find_edges.png",'png')

# convert into black and white old looking
my_image_bnw = my_image.convert('LA')
my_image_bnw.save('bnws.jpg','png')