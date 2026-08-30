import qrcode
data =input("Enter text or link: ")
img=qrcode.make(data)
img.save("img.png")
img.show()
print("QR code generated successfully!!")