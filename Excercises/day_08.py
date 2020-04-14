import requests
import json
import bs4
import urllib.request
# site = requests.get("https://wp.pl")
# # print(site.text)
#
# data = requests.get("https://api.exchangeratesapi.io/2000-01-03")
# print(type(data.text))
# # data_json = data.json()
# # print(data_json)
# # # print(data_json['rates']["PLN"])
# #
# # data_json = json.loads(data)
# # print(data_json["rates"]["PLN"])
# olx_html = requests.get("https://www.olx.pl/motoryzacja/samochody/")
# parser = bs4.BeautifulSoup(olx_html.text, 'html.parser')
# i = 0
# obrazki = parser.find_all('img')
# for pic in obrazki:
#     nazwa = (pic.get('alt'))
#     adres = (pic.get('src'))
#     obrazek = requests.get(adres).content
#     with open(f"obrazki/pic_{i}.jpg", "wb") as plik:
#         plik.write(obrazek)
#         i += 1

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail = MIMEMultipart()
mail["Subject"] = "Temat"
mail["To"] = 'kaja.kinga.rudnicka@gmail.com'
mail["From"] = "isapy@int.pl"
text = MIMEText('Mail o niczym')
mail.attach(text)
with smtplib.SMTP('poczta.int.pl') as serwer:
    serwer.login('isapy@int.pl', 'isapython;')