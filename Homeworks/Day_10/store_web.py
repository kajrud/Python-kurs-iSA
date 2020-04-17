import flask
import Homeworks.Day_10.model.model as store

app = flask.Flask(__name__)
# app.debug = True

@app.route("/")
def main():
    return flask.render_template("index.html")

@app.route("/our-books")
def our_books():
    return flask.render_template("offer.html")

@app.route("/potop")
@app.route("/krzyzacy")
@app.route("/lotr")
def add_to_cart():
    cart = store.Cart()
    cart.dodaj(element)




app.run()