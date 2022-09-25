import smtplib

from flask import render_template, flash, redirect, url_for, current_app
from flask_login import login_user, logout_user, login_required, current_user
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from app import app, db, login_manager

from app.models.tables import User
from app.models.forms import LoginForm, RegisterForm


@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/index")
@app.route("/")
def index():
    users = User.query.filter_by(username="ems").all()
    for user in users:
        print(user.profile)
    return render_template("index.html")


@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logado com sucesso")
            return redirect(url_for("index"))
        else:
            flash("Login inválido")
    else:
        print(form.errors)

    return render_template("login.html", form=form)


@login_required
@app.route("/logout")
def logout():
    logout_user()
    flash("Deslogado")
    return redirect(url_for("index"))


@app.route("/sign_up", methods=["GET","POST"])
def sign_up():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            NewUserData = User(form.username.data, form.email.data, form.password.data, form.name.data, profile="follower")
            print(NewUserData)
            db.session.add(NewUserData)
            db.session.commit()
            return redirect(url_for("index"))
        except:
            return redirect(url_for("index"))
    else:
        print(form.errors)
    return render_template('sign_up.html', form=form)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if current_user.is_authenticated == True:
        user = User.query.filter_by(id=current_user.id).first()
        return render_template('my_profile.html', profile=user)
    else:
        redirect(url_for("login"))


@app.route("/delete-user", methods=['GET', 'POST'])
def delete_user():
    if current_user.is_authenticated == True:
        user = User.query.filter_by(id=current_user.id).first()
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for("index"))


@app.route("/send_mail", methods=["POST"])
def send_mail():
    email_list = []
    users = User.query.all()
    for user in users:
        email_list.append(user.email)

    # Configurar e-mail e senha
    EMAIL_ADDRESS = 'emilycolona27@gmail.com'
    EMAIL_PASSWORD = current_app.config.get('PASSWORD_KEY')

    mail_body = render_template("notification_email.html")
    
    # Cria o e-mail
    msg = MIMEMultipart()
    msg['Subject'] = 'BiggyGlue está ao vivo na TWITCH!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'emilycolona27@gmail.com'

    msg.attach(MIMEText(mail_body, 'html'))

    img_src = "E:\\Templates Novos\\Code\\Send Mail\\app\\static\\goat.jpg"
    attachment = open(img_src, 'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attachment.read())
    encoders.encode_base64(att)

    att.add_header('Content-Disposition', f'attachment; filename=goat.jpg')
    attachment.close()
    msg.attach(att)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.ehlo()
    s.starttls()

    # Credenciais de login para enviar o e-mail
    s.login(msg['From'], EMAIL_PASSWORD)
    s.sendmail(msg['From'], email_list, msg.as_string().encode('utf-8'))
    s.quit()
    flash("E-mail enviado, boa live :)")

    return redirect(url_for("profile"))
