from app import app
from db import db
import quizzes
from flask import render_template, request, redirect
from sqlalchemy import text

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    if request.method=="POST" and request.form["userRadio"]=="user":
        return redirect("/user")
    else:
        return redirect("/admin")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        return redirect("/user")

@app.route("/logout")
def logout():
    return render_template("logout.html")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method=="GET":
        dict_quizzes = quizzes.show_quizzes_toadmin()
        print(dict_quizzes)
        return render_template("admin.html", dict_quizzes=dict_quizzes)
    else:
        quizname=request.form["quizname"]
        question=request.form["question1"]
        option1=request.form["option1"]
        option2=request.form["option2"]
        option3=request.form["option3"]
        correctoption=request.form["correctoption"]
        quizzes.create_quiz(quizname)
        quizid = quizzes.get_quizid(quizname)
        quizzes.add_question(quizid, question)
        questionid = quizzes.get_questionid(question)
        quizzes.add_options(questionid, option1)
        quizzes.add_options(questionid, option2)
        quizzes.add_options(questionid, option3)
        optionid = quizzes.get_optionid(correctoption)
        quizzes.add_correctoption(optionid)
        dict_quizzes = quizzes.show_quizzes_toadmin()
        return render_template("admin.html", dict_quizzes=dict_quizzes)

@app.route("/user")
def user():
    return render_template("user.html")

@app.route("/accountremoved")
def accountremoved():
    return render_template("accountremoved.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method=="GET":
        return render_template("quiz.html")
    else:
        return redirect("/quizresult")
    
@app.route("/quizresult")
def quizresult():
    return render_template("quizresult.html")

@app.route("/newquiz", methods=["GET", "POST"])
def newquiz():
    if request.method=="GET":
        return render_template("newquiz.html")
    else:
        quizname=request.form["quizname"]
        if quizzes.check_quizname(quizname)==True:
            error = (f"Quiz name {quizname} already exists. Please choose a different one.")
            return render_template("newquiz.html", error=error)
        else:
            return render_template("newquiz.html")
        return redirect("/admin")