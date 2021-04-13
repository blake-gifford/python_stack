from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", phrase = "Hello", times = 5)


@app.route("/dojo")
def dojo():
    return "Welcome to the Dojo!"


@app.route("/<string:name>")
def _name(name):
    return f"Hello {name}!!!"


@app.route("/<name>/<int:num>")
def name_name(name, num):
    return f"Hello {name}," * {num}


if __name__ == "__main__":
    app.run(debug = True)

