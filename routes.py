from app import app
from db import db
import quizzes
import users
from flask import render_template, request, redirect, session
from sqlalchemy import text

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    else:
        username=request.form["username"]
        if users.check_username(username)==True:
            error = (f"Username {username} already exists. Please choose a different one.")
            return render_template("register.html", error=error)
        else:
            users.create_user(username)
            return render_template("register.html", username=username)
        
@app.route("/registersuccess", methods=["GET","POST"])
def registersuccess():
    if request.method=="GET":
        return render_template("registersuccess.html")
    else:
        username=request.form["username"]
        password=request.form["password"]
        admin=request.form["userradio"]
        gdpr=request.form["gdprcheck"]
        print(users.register(username, password, admin, gdpr))
        return render_template("registersuccess.html", username=username)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            if users.check_ifadmin(username):
                return redirect("/admin")
            else:
                return redirect("/user")
        else:
            error = {f"Username or password failed, try again"}
            return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    del session["username"]
    return render_template("logout.html")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method=="GET":
        username = session["username"]
        dict_quizzes = quizzes.show_quizzes_toadmin(username)
        #print(dict_quizzes)
        return render_template("admin.html", dict_quizzes=dict_quizzes)
    else:
        quizname=request.form["quizname"]
        question1=request.form["question1"]
        option11=request.form["option11"]
        option12=request.form["option12"]
        option13=request.form["option13"]
        correctoption1=request.form["correctoption1"]
        question2=request.form["question2"]
        option21=request.form["option21"]
        option22=request.form["option22"]
        option23=request.form["option23"]
        correctoption2=request.form["correctoption2"]
        question3=request.form["question3"]
        option31=request.form["option31"]
        option32=request.form["option32"]
        option33=request.form["option33"]
        correctoption3=request.form["correctoption3"]
        question4=request.form["question4"]
        option41=request.form["option41"]
        option42=request.form["option42"]
        option43=request.form["option43"]
        correctoption4=request.form["correctoption4"]
        question5=request.form["question5"]
        option51=request.form["option51"]
        option52=request.form["option52"]
        option53=request.form["option53"]
        correctoption5=request.form["correctoption5"]
        #quizzes.create_quiz(quizname)
        quizid = quizzes.get_quizid(quizname)
        quizzes.add_question(quizid, question1)
        questionid = quizzes.get_questionid(question1)
        quizzes.add_options(questionid, option11)
        quizzes.add_options(questionid, option12)
        quizzes.add_options(questionid, option13)
        optionid = quizzes.get_optionid(correctoption1)
        quizzes.add_correctoption(optionid)
        quizzes.add_question(quizid, question2)
        questionid = quizzes.get_questionid(question2)
        quizzes.add_options(questionid, option21)
        quizzes.add_options(questionid, option22)
        quizzes.add_options(questionid, option23)
        optionid = quizzes.get_optionid(correctoption2)
        quizzes.add_correctoption(optionid)
        quizzes.add_question(quizid, question3)
        questionid = quizzes.get_questionid(question3)
        quizzes.add_options(questionid, option31)
        quizzes.add_options(questionid, option32)
        quizzes.add_options(questionid, option33)
        optionid = quizzes.get_optionid(correctoption3)
        quizzes.add_correctoption(optionid)
        quizzes.add_question(quizid, question4)
        questionid = quizzes.get_questionid(question4)
        quizzes.add_options(questionid, option41)
        quizzes.add_options(questionid, option42)
        quizzes.add_options(questionid, option43)
        optionid = quizzes.get_optionid(correctoption4)
        quizzes.add_correctoption(optionid)
        quizzes.add_question(quizid, question5)
        questionid = quizzes.get_questionid(question5)
        quizzes.add_options(questionid, option51)
        quizzes.add_options(questionid, option52)
        quizzes.add_options(questionid, option53)
        optionid = quizzes.get_optionid(correctoption5)
        quizzes.add_correctoption(optionid)
        username = session["username"]
        dict_quizzes = quizzes.show_quizzes_toadmin(username)
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
        quizname = request.form["quizname"]
        username = session["username"]
        if quizzes.check_quizname(quizname)==True:
            error = (f"Quiz name {quizname} already exists. Please choose a different one.")
            return render_template("newquiz.html", error=error)
        else:
            quizzes.create_quiz(quizname, username)
            return render_template("newquiz.html", quizname=quizname)
        
@app.route("/adminquiz/<int:quiz_id>", methods=["GET", "POST"])
def adminquiz(quiz_id):
    if request.method=="GET":
        quizname = quizzes.get_quizname(quiz_id)
        status = quizzes.get_published(quiz_id)
        return render_template("adminquiz.html", quiz_id=quiz_id, quizname=quizname, published=status)
    else:
        published = request.form["published"]
        quizzes.publish_quiz(quiz_id, published)
        quizname = quizzes.get_quizname(quiz_id)
        status = quizzes.get_published(quiz_id)
        return render_template("adminquiz.html", quiz_id=quiz_id, quizname=quizname, published=status)