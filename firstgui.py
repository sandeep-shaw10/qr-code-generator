#Importing modules
import eel
import qrcode
import qrcode.image.svg

#Initializing the frontend directory
eel.init("web")

#Function
@eel.expose
def display():
    return "Python Eel"

@eel.expose
def generateQRCode(name, fileName, ext):
    ext = int(ext)
    if(ext==3):
        qr = qrcode.image.svg.SvgPathImage
        img = qrcode.make(name, image_factory = qr)
        img.save(f"web/QRcode/{fileName}.svg")
        ext = "svg"
    else:
        #object of qrcode
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_H, 
            box_size = 10,border = 4,
        )

        qr.add_data(name)
        qr.make(fit=True)
        img = qr.make_image()

        if(ext==0):
            img.save(f"web/QRcode/{fileName}.jpg")
            ext = "jpg"
        elif(ext==1):
            img.save(f"web/QRcode/{fileName}.jpeg")
            ext = "jpeg"
        elif(ext==2):
            img.save(f"web/QRcode/{fileName}.png")
            ext = "png"
        else:
            img.save(f"web/QRcode/{fileName}.bmp")
            ext = "bmp"
    return fileName+"."+ext

#Call the frontend
eel.start("base.html",size=(1000,550))

