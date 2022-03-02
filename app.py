from distutils.log import debug
import datetime
from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='template', static_folder='static')


@app.route("/")
def login():
    return render_template("login.html", utc_dt=datetime.datetime.utcnow())


@app.route("/general")
def gen_details():
    return render_template("gen details.html")


@app.route("/student")
def student():
    return render_template("student.html")


@app.route("/start")
def start():
    return render_template("start.html")


@app.route("/result")
def result():
    return render_template("result.html")


@app.route("/teacher")
def teacher():
    return render_template("teacher.html")


@app.route("/statistics")
def statistics():
    return render_template("statistics.html")


@app.route("/question")
def question():
    return render_template("question.html")


@app.route("/view")
def view():
    return render_template("view question.html")


@app.route("/report")
def report():
    return render_template("report.html")


@app.route("/mcq")
def mcq():
    return render_template("mcq.html")


if __name__ == "__main__":
    app.run(debug=True)
