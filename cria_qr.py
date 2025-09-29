import qrcode

# Texto ou URL para gerar o QR Code
data = "https://colab.research.google.com/drive/1kxHuC_wf804aKDSJvHikCqyDv9CS4b_8"

# Gerar o QR Code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(data)
qr.make(fit=True)

# Criar imagem do QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Salvar imagem
img.save("qrcode.png")

print("QR Code gerado e salvo como qrcode.png")