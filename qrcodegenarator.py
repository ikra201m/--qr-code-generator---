import qrcode
import image
qr=qrcode.QRCode(
    version= 15, #version of qr code
    box_size=10, #size of the box where qr will be displayed
    border=5 #white part of the image
)
data ="Ikram Hossain |\nB.sc(Mathematics),3rd Year\n|Department of Mathematics ,University of Dhaka\n|Resident,Amar Ekushey Hall"
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color = "white")
img.save("test.png")