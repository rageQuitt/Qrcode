import qrcode
#pip install qrcode[pil]

data = "Be Impeccable with you words"
qr = qrcode.QRCode(
    version=1, #taille du Qrcode
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data) #ajout les données
qr.make(fit=True) #finalise le QR code

img = qr.make_image(fill_color="black", back_color="white") #crée une image du QR code avec un remplissage 
img.save('qrcode.png') # sauvegarde l'image du QR code dans le répertoire 

img.show() #genere l'image dans le meme répertoire

#Dans le terminal : python main.py

