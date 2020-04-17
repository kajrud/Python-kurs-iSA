from flask import Flask, render_template, request, url_for

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/formularz", methods = "POST")
def formularz():
    name = (request.form['name'])
    age = (request.form["age"])
    return hello2(name, age)

@app.route("/witaj")
@app.route("/witaj/<name>")
@app.route(("/witaj/<name>/<int:age>"))
def hello2(name = "", age = 3):
    name = name.capitalize()
    # print(f"Witaj {name}! Masz {age} lat.")
    print(url_for("hello2", name="Ewa"))
    return render_template("index.html", t_name = name, t_age = age)

@app.route("/kwadrat/<int:num>")
def kwadrat(num):
    return f"Kwadrat liczby {num} to {num ** 2}."

# @app.route("/")
# @app.route('/list')
# def list():
#
#     return render_template("list.html", )
# @app.route('/login', methods = ["GET", "POST"])
# def login():
#     if request.method == "POST":



app.run()