import smtplib
import email.message

from flask import Flask, render_template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from secret_data import password

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

@app.route("/")
def index():
    return "hello world"
    # return render_template("app/index.html")

# @app.route("/send_mail", methods=["POST"])
# def send_mail():
#     # Configurar e-mail e senha
#     EMAIL_ADDRESS = 'emilycolona27@gmail.com'
#     EMAIL_PASSWORD = password

#     mail_body = render_template("notification_email.html")
    
#     # Cria o e-mail
#     msg = MIMEMultipart()
#     msg['Subject'] = 'BiggyGlue está ao vivo na TWITCH!'
#     msg['From'] = EMAIL_ADDRESS
#     # msg['To'] = 'emilycolona@hotmail.com'
#     msg['To'] = 'emilycolona27@gmail.com'

#     msg.attach(MIMEText(mail_body, 'html'))

#     img_src = "E:\\Templates Novos\\Code\\Send Mail\\templates\\img\\goat.jpg"
#     attachment = open(img_src, 'rb')
#     att = MIMEBase('application', 'octet-stream')
#     att.set_payload(attachment.read())
#     encoders.encode_base64(att)

#     att.add_header('Content-Disposition', f'attachment; filename=goat.jpg')
#     attachment.close()
#     msg.attach(att)

#     s = smtplib.SMTP('smtp.gmail.com: 587')
#     s.ehlo()
#     s.starttls()

#     # Credenciais de login para enviar o e-mail
#     s.login(msg['From'], EMAIL_PASSWORD)
#     s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
#     s.quit()
#     print('E-mail enviado :)')

#     return "E-mail enviado!"


if __name__ == "__main__":
    app.run(debug=True)