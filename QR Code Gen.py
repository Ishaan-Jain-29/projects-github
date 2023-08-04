import qrcode, os, PIL
def make():
    image = qrcode.make(input("Text or URL: "))
    image.save("qrcode.png")
    img = PIL.Image.open("qrcode.png")
    img.show()
    os.remove("qrcode.png")
    make()
make()