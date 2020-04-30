import flask
import Homeworks.Day_10.model.model as store

baza = store.Db("model/db.csv")
cart = store.Cart()
len_store = len(baza.database)

app = flask.Flask(__name__)
app.debug = True


@app.route("/")
def main():
    return flask.render_template("index.html")

@app.route("/our-books")
def our_books():
    return flask.render_template("offer.html", store=baza.database, len_store=len(baza.database))

@app.route('/added-to-cart')
def add_to_cart(element):

    cart = store.Cart()
    cart.dodaj(element)
    print("Dodano element")
    print(cart)
    return flask.render_template("add_to_cart.html")

@app.route("/cart")
def view_cart():
    return cart.cart_view()
    # return flask.render_template("view_cart.html")

app.run()