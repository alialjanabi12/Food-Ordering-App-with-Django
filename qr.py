import qrcode

# CREATING A QR CODE
image = qrcode.make("https://127.0.0.1:8000")
image.save("qr.png")
