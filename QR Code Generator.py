import qrcode as q

data = 'Like, Share and Subscribe'
qr = q.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
img = q.make(data)
img.save(r'D:\Video_block\Python_program\Python Mini Project\QRcode.png')