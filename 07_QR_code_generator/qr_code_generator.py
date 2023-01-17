'''
1) install all the libraries needed
2) Create a function that collects a text and converts it to a qrcode
3) save the qrcode as an image
4) run the function
'''
import qrcode


def generate_qrcode(text):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")


url = input("Enter your url: ")
generate_qrcode(url)
