import flask
import requests
from bs4 import BeautifulSoup

app = flask.Flask(__name__)
app.debug = True

@app.route("/", methods = ['POST', 'GET'])
def basic():
    return flask.render_template("day_13.html")

@app.route('/form', methods=['POST'])
def formularz():
    list = []
    url = flask.request.form['url']
    print(url)
    type = flask.request.form['typ']
    if type == 'obrazy':
        website = requests.get(url).text
        parser = BeautifulSoup(website, 'html.parser')
        i = 0
        obrazki = parser.find_all('img')
        for pic in obrazki:
            name = (pic.get('alt'))
            source = (pic.get('src'))
            list.append([name, source])

    elif type == 'dokumenty':
        website = requests.get(url).text

        pass
    else:
        pass

    mail = flask.request.form['email']
    print(mail)
    if mail is not "":
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        mail = MIMEMultipart()
        mail["Subject"] = "Pobieraczek"
        mail["To"] = mail
        mail["From"] = "isapy@int.pl"
        text = MIMEText('Pliki w załączniku')
        mail.attach(text)
        mail.attach(list)
        with smtplib.SMTP('poczta.int.pl') as serwer:
            serwer.login('isapy@int.pl', 'isapython;')
    else:
        print("No email!")
    return flask.render_template('day_13.html', lista_plikow = list)




app.run()