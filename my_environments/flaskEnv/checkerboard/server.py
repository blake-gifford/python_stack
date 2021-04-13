from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", num = 4, num1 = 4)

@app.route("/<int:num>")
def board_size(num):
    return render_template("index.html", num = num, num1 = num)


@app.route("/<int:num>/<int:num1>")
def x_y_board(num,num1):
    return render_template("index.html", num = num, num1 = num1)


if __name__ == "__main__":
    app.run(debug = True)

