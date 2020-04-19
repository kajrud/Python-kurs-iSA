import flask
import Homeworks.Day_10.model.model as store

baza = store.Db("model/db.csv")
potop = baza.database[1]
krzyzacy = baza.database[2]
lotr = baza.database[3]

cart = store.Cart()

app = flask.Flask(__name__)
app.debug = True

@app.route("/")
def main():
    return flask.render_template("index.html")

@app.route("/our-books")
def our_books():
    return flask.render_template("offer.html")

@app.route("/<element>", methods = ["GET", "POST"])
def add_to_cart(element):
    cart = store.Cart()
    cart.dodaj(element)
    return flask.render_template("add_to_cart.html")

@app.route("/cart")
def view_cart():
    return cart.cart_view()
    # return flask.render_template("view_cart.html")

app.run()