# 必要なライブラリをインポート
import csv
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# GmailのSMTPサーバーの情報
smtp_server = "smtp.gmail.com"
port = 587

# 送信元のGmailアドレスとアプリパスワード
sender_email = "*******@gmail.com"
password = "*****"

# メールの件名
subject = "test:弊社製品に関するアンケートのお願い"

# テキストファイルからメール本文を読み込む
with open("message.txt", "r", encoding="utf-8") as f:
    message_template = f.read()

# csvファイルから宛先リストを読み込む
with open("list.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader) # ヘッダー行をスキップ
    recipients = list(reader) # 宛先リストをリスト型に変換

# SSLコンテキストを作成
context = ssl.create_default_context()

# SMTPサーバーに接続してメール送信処理を開始
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    # TLS暗号化を開始
    server.starttls(context=context)
    server.ehlo()

    # Gmailアカウントにログイン
    server.login(sender_email, password)

    # 宛先リストの各要素に対してメール送信処理を繰り返す
    for name, email in recipients:
        # メールの本文を作成
        message = message_template.format(name=name)

        # メールのオブジェクトを作成
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = email
        msg["Subject"] = subject

        # メールの本文をオブジェクトに追加
        msg.attach(MIMEText(message, "plain"))

        # メールを送信
        server.sendmail(sender_email, email, msg.as_string())
        print(f"Sent email to {name} at {email}")

    # SMTPサーバーとの接続を終了
    server.quit()

except Exception as e:
    # エラーが発生した場合は表示
    print(e)
