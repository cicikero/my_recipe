import csv
import qrcode

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

# CSVファイルからデータとファイル名を読み込んでQRコードを生成
with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data = row[0]
        file_name = row[1]
        generate_qr_code(data, file_name)

"""
data.csv の書式は以下。

Hello, QR Code 1,qrcode1.png
Hello, QR Code 2,qrcode2.png
Hello, QR Code 3,qrcode3.png

"""