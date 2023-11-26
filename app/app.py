from flask import Flask, request, Response
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

app = Flask(__name__)
@app.route('/email-webhook', methods=['POST'])

def return_response():
    # Read the content from post message
    data = request.json
    message = data['text']

    try:
        content = MIMEMultipart()
        content["subject"] = "Sample Python Email webhook"
        content["from"] = "sample@gmail.com" # Sender email
        content["to"] = "receiver@gmail.com" # Receiver email
        content["cc"] = "" # CC email (if any)
        content.attach(MIMEText(message,'plain')) # Print the content from webhook
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.ehlo()  # SMTP Helo
        smtp.starttls()  # Encrypt
        smtp.login("sample@gmail.com", "應用程式密碼")  # Sender gmail address	
        smtp.send_message(content)
    except Exception as e:
        print("Error message: ", e)

    return Response(status=200)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
