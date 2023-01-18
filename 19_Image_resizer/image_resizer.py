'''
install pillow
import pillow
open the image needed to resize using python
print the current size 
specify the size we want to change it to
save the new resized image
'''

from PIL import Image


def resize_image(size1, size2):
    image = Image.open("test.jpg")

    print(f"Current size: {image.size}")

    resized_image = image.resize((size1, size2))

    resized_image.save(f'resized_test_({size1},{size2}).jpg')


size1 = int(input("Enter Width: "))
size2 = int(input("Enter Length: "))

resize_image(size1, size2)
