import qrcode
import image

qr = qrcode.QRCode(version=5,
box_size=10,
border=3)

data = """Muhammed Tekin GitHub
https://github.com/tekinmuhammed
"""
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black",back_color = "white")
img.save("qr.png")