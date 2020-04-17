import flask

app = flask.Flask(__name__)
app.debug = True

@app.route("/")
def main():
    return flask.render_template("index.html")

@app.route("/our-books")
def our_books():
    pass

@app.route()

app.run()