from flask import render_template, request, redirect, session, abort
from app import app
import quizzes
import users


@app.route("/")
def index():
    published_quizzes = quizzes.show_published_quizzes()
    leaderboard = users.calculate_leaderboard()
    ratings = quizzes.calculate_ratings()
    return render_template("index.html", ratings=ratings,
                           published_quizzes=published_quizzes, leaderboard=leaderboard)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form["username"]
        if users.check_username(username):
            message = f"Username {username} already exists. Please choose a different one."
            return render_template("register.html", message=message)
        else:
            message = f"Success! Please continue to set your password."
            return render_template("register.html", username=username, message=message)

@app.route("/registersuccess", methods=["GET", "POST"])
def registersuccess():
    if request.method == "GET":
        return render_template("registersuccess.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        admin = request.form["userradio"]
        gdpr = request.form["gdprcheck"]
        users.create_user(username)
        users.register(username, password, admin, gdpr)
        return render_template("registersuccess.html", username=username)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        if not users.login(username, password):
            error = f"Username or password failed, please try again."
            return render_template("login.html", error=error)
        else:
            if users.check_ifadmin(username):
                return redirect("/admin")
            else:
                return redirect("/user")

@app.route("/logout")
def logout():
    if "username" in session:
        del session["username"]
        return render_template("logout.html")
    else:
        return redirect("/")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "GET":
        if "username" in session:
            username = session["username"]
            dict_quizzes = quizzes.show_quizzes_toadmin(username)
            message = f"You don't have any quizzes yet."
            correct_answers = users.calculate_correctanswers(username)
            played_quizzes = users.calculate_playedquizzes(username)
            played_quiznames = users.show_playedquizzes(username)
            message2 = f"0"
            own_quizzes = users.calculate_playedquizzes_created(username)
            own_quizzes_canswers = users.calculate_correctanswers_created(username)
            own_quizzes_answers = users.calculate_allanswers_created(username)
            return render_template("admin.html", own_quizzes_canswers=own_quizzes_canswers,
                                   own_quizzes_answers=own_quizzes_answers, own_quizzes=own_quizzes,
                                   message2=message2, dict_quizzes=dict_quizzes, message=message,
                                   correct_answers=correct_answers, played_quizzes=played_quizzes,
                                   played_quiznames=played_quiznames)
        else:
            return render_template("admin.html")
    else:
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        else:
            username = request.form["username"]
            quizname = request.form["quizname"]
            category = request.form["category"]
            question1 = request.form["question1"]
            option11 = request.form["option11"]
            option12 = request.form["option12"]
            option13 = request.form["option13"]
            question2 = request.form["question2"]
            option21 = request.form["option21"]
            option22 = request.form["option22"]
            option23 = request.form["option23"]
            question3 = request.form["question3"]
            option31 = request.form["option31"]
            option32 = request.form["option32"]
            option33 = request.form["option33"]
            question4 = request.form["question4"]
            option41 = request.form["option41"]
            option42 = request.form["option42"]
            option43 = request.form["option43"]
            question5 = request.form["question5"]
            option51 = request.form["option51"]
            option52 = request.form["option52"]
            option53 = request.form["option53"]
            questions = [question1, question2, question3, question4, question5]
            if len(questions) != len(set(questions)):
                error = f"""All questions must be unique, you can't have same question repeated in a quiz.
                Please check your questions again. Remember to choose the category as well."""
                return render_template("newquiz.html", error=error, username=username,
                                       quizname=quizname, category=category,
                                       question1=question1, option11=option11, option12=option12,
                                       option13=option13, question2=question2, option21=option21,
                                       option22=option22, option23=option23, question3=question3,
                                       option31=option31, option32=option32, option33=option33,
                                       question4=question4, option41=option41, option42=option42,
                                       option43=option43, question5=question5, option51=option51,
                                       option52=option52, option53=option53)
            else:
                quizzes.create_quiz(quizname, username)
                quizid = quizzes.get_quizid(quizname)
                quizzes.add_category(quizid, category)
                quizzes.add_question(quizid, question1)
                questionid = quizzes.get_questionid(question1, quizid)
                quizzes.add_options(questionid, option11)
                quizzes.add_options(questionid, option12)
                quizzes.add_options(questionid, option13)
                quizzes.add_question(quizid, question2)
                questionid = quizzes.get_questionid(question2, quizid)
                quizzes.add_options(questionid, option21)
                quizzes.add_options(questionid, option22)
                quizzes.add_options(questionid, option23)
                quizzes.add_question(quizid, question3)
                questionid = quizzes.get_questionid(question3, quizid)
                quizzes.add_options(questionid, option31)
                quizzes.add_options(questionid, option32)
                quizzes.add_options(questionid, option33)
                quizzes.add_question(quizid, question4)
                questionid = quizzes.get_questionid(question4, quizid)
                quizzes.add_options(questionid, option41)
                quizzes.add_options(questionid, option42)
                quizzes.add_options(questionid, option43)
                quizzes.add_question(quizid, question5)
                questionid = quizzes.get_questionid(question5, quizid)
                quizzes.add_options(questionid, option51)
                quizzes.add_options(questionid, option52)
                quizzes.add_options(questionid, option53)
                dict_quizzes = quizzes.show_quizzes_toadmin(username)
                return render_template("admin.html", dict_quizzes=dict_quizzes)

@app.route("/user")
def user():
    if "username" in session:
        username = session["username"]
        correct_answers = users.calculate_correctanswers(username)
        played_quizzes = users.calculate_playedquizzes(username)
        played_quiznames = users.show_playedquizzes(username)
        leaderboard = users.calculate_leaderboard()
        message = f"0"
        return render_template("user.html", message=message, leaderboard=leaderboard,
                               correct_answers=correct_answers, played_quizzes=played_quizzes,
                               played_quiznames=played_quiznames)
    else:
        return render_template("user.html")

@app.route("/accountremoved", methods=["GET", "POST"])
def accountremoved():
    if request.method == "GET":
        return render_template("accountremoved.html")
    else:
        username = session["username"]
        remove_user = request.form["userremove"]
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        else:
            if remove_user:
                if users.check_ifadmin(username):
                    users.remove_user(username)
                    quizzes.delete_answer(username)
                    quizzes.delete_quiz(username)
                    quizzes.delete_rating(username)
                    del session["username"]
                    return render_template("accountremoved.html")
                else:
                    users.remove_user(username)
                    quizzes.delete_answer(username)
                    quizzes.delete_rating(username)
                    del session["username"]
                    return render_template("accountremoved.html")

@app.route("/quiz/<int:quiz_id>", methods=["GET", "POST"])
def quiz(quiz_id):
    if request.method == "GET":
        quizname = quizzes.get_quizname(quiz_id)
        questions = quizzes.get_questions(quiz_id)
        question1 = questions[0][0]
        question2 = questions[1][0]
        question3 = questions[2][0]
        question4 = questions[3][0]
        question5 = questions[4][0]
        options1 = quizzes.get_options(quiz_id, question1)
        options2 = quizzes.get_options(quiz_id, question2)
        options3 = quizzes.get_options(quiz_id, question3)
        options4 = quizzes.get_options(quiz_id, question4)
        options5 = quizzes.get_options(quiz_id, question5)
        leaderboard = users.calculate_leaderboard()
        ratings = quizzes.calculate_ratings()
        return render_template("quiz.html", ratings=ratings, leaderboard=leaderboard,
                               quiz_id=quiz_id, quizname=quizname, options1=options1,
                               options2=options2, options3=options3, options4=options4,
                               options5=options5, questions=questions)
    else:
        return redirect("/")

@app.route("/quizresult", methods=["GET", "POST"])
def quizresult():
    if request.method == "GET":
        return render_template("quizresult.html")
    else:
        if "username" in session:
            username = session["username"]
        else:
            username = "guest"
        correct_answers = 0
        answers = []
        quiz_id = request.form["quiz_id"]
        if not users.check_ifplayed(quiz_id, username) and username != "guest":
            if session["csrf_token"] != request.form["csrf_token"]:
                abort(403)
            else:
                question1_answer = request.form["quizOptions1"]
                answers.append(quizzes.get_option(question1_answer))
                quizzes.save_answer(username, question1_answer, quiz_id)
                if quizzes.check_ifcorrectoption(question1_answer):
                    correct_answers += 1
                question2_answer = request.form["quizOptions2"]
                answers.append(quizzes.get_option(question2_answer))
                quizzes.save_answer(username, question2_answer, quiz_id)
                if quizzes.check_ifcorrectoption(question2_answer):
                    correct_answers += 1
                question3_answer = request.form["quizOptions3"]
                answers.append(quizzes.get_option(question3_answer))
                quizzes.save_answer(username, question3_answer, quiz_id)
                if quizzes.check_ifcorrectoption(question3_answer):
                    correct_answers += 1
                question4_answer = request.form["quizOptions4"]
                answers.append(quizzes.get_option(question4_answer))
                quizzes.save_answer(username, question4_answer, quiz_id)
                if quizzes.check_ifcorrectoption(question4_answer):
                    correct_answers += 1
                question5_answer = request.form["quizOptions5"]
                answers.append(quizzes.get_option(question5_answer))
                quizzes.save_answer(username, question5_answer, quiz_id)
                if quizzes.check_ifcorrectoption(question5_answer):
                    correct_answers += 1
                question1_id = quizzes.get_questionid_option(question1_answer)
                question2_id = quizzes.get_questionid_option(question2_answer)
                question3_id = quizzes.get_questionid_option(question3_answer)
                question4_id = quizzes.get_questionid_option(question4_answer)
                question5_id = quizzes.get_questionid_option(question5_answer)
                correct_answer1 = quizzes.get_correctoption_label(question1_id)
                correct_answer2 = quizzes.get_correctoption_label(question2_id)
                correct_answer3 = quizzes.get_correctoption_label(question3_id)
                correct_answer4 = quizzes.get_correctoption_label(question4_id)
                correct_answer5 = quizzes.get_correctoption_label(question5_id)
                leaderboard = users.calculate_leaderboard()
                ratings = quizzes.calculate_ratings()
                return render_template("quizresult.html", ratings=ratings, quiz_id=quiz_id,
                                       leaderboard=leaderboard, answers=answers,
                                       correct_answers=correct_answers, correct_answer1=correct_answer1,
                                       correct_answer2=correct_answer2, correct_answer3=correct_answer3,
                                       correct_answer4=correct_answer4, correct_answer5=correct_answer5)
        else:
            question1_answer = request.form["quizOptions1"]
            answers.append(quizzes.get_option(question1_answer))
            if quizzes.check_ifcorrectoption(question1_answer):
                correct_answers += 1
            question2_answer = request.form["quizOptions2"]
            answers.append(quizzes.get_option(question2_answer))
            if quizzes.check_ifcorrectoption(question2_answer):
                correct_answers += 1
            question3_answer = request.form["quizOptions3"]
            answers.append(quizzes.get_option(question3_answer))
            if quizzes.check_ifcorrectoption(question3_answer):
                correct_answers += 1
            question4_answer = request.form["quizOptions4"]
            answers.append(quizzes.get_option(question4_answer))
            if quizzes.check_ifcorrectoption(question4_answer):
                correct_answers += 1
            question5_answer = request.form["quizOptions5"]
            answers.append(quizzes.get_option(question5_answer))
            if quizzes.check_ifcorrectoption(question5_answer):
                correct_answers += 1
            question1_id = quizzes.get_questionid_option(question1_answer)
            question2_id = quizzes.get_questionid_option(question2_answer)
            question3_id = quizzes.get_questionid_option(question3_answer)
            question4_id = quizzes.get_questionid_option(question4_answer)
            question5_id = quizzes.get_questionid_option(question5_answer)
            correct_answer1 = quizzes.get_correctoption_label(question1_id)
            correct_answer2 = quizzes.get_correctoption_label(question2_id)
            correct_answer3 = quizzes.get_correctoption_label(question3_id)
            correct_answer4 = quizzes.get_correctoption_label(question4_id)
            correct_answer5 = quizzes.get_correctoption_label(question5_id)
            message = f"""The result wasn't saved. Are you a guest user?
            Or you have already played this quiz."""
            leaderboard = users.calculate_leaderboard()
            ratings = quizzes.calculate_ratings()
            return render_template("quizresult.html", ratings=ratings, quiz_id=quiz_id,
                                   leaderboard=leaderboard, message=message, answers=answers,
                                   correct_answers=correct_answers, correct_answer1=correct_answer1,
                                   correct_answer2=correct_answer2, correct_answer3=correct_answer3,
                                   correct_answer4=correct_answer4, correct_answer5=correct_answer5)

@app.route("/newquiz", methods=["GET", "POST"])
def newquiz():
    if request.method == "GET":
        return render_template("newquiz.html")
    else:
        quizname = request.form["quizname"]
        username = session["username"]
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        else:
            if quizzes.check_quizname(quizname):
                message = f"Quiz name {quizname} already exists. Please choose a different one."
                return render_template("newquiz.html", message=message)
            else:
                message = (f"""Success! Please continue to choose a category and set questions and options.
                           Submit all questions and options at once, you can't edit them later. 
                           All fields are required and questions must be unique.""")
                return render_template("newquiz.html", quizname=quizname, username=username,
                                       message=message)

@app.route("/adminquiz/<int:quiz_id>", methods=["GET", "POST"])
def adminquiz(quiz_id):
    if request.method == "GET":
        quizname = quizzes.get_quizname(quiz_id)
        status = quizzes.get_published(quiz_id)
        questions = quizzes.get_questions(quiz_id)
        question1 = questions[0][0]
        question2 = questions[1][0]
        question3 = questions[2][0]
        question4 = questions[3][0]
        question5 = questions[4][0]
        options1 = quizzes.get_options(quiz_id, question1)
        options2 = quizzes.get_options(quiz_id, question2)
        options3 = quizzes.get_options(quiz_id, question3)
        options4 = quizzes.get_options(quiz_id, question4)
        options5 = quizzes.get_options(quiz_id, question5)
        return render_template("adminquiz.html", quiz_id=quiz_id, quizname=quizname,
                               published=status, options1=options1, options2=options2,
                               options3=options3, options4=options4, options5=options5,
                               questions=questions)
    else:
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        else:
            published = request.form["published"]
            quizzes.publish_quiz(quiz_id, published)
            correctoption1 = request.form["correctoption1"]
            quizzes.add_correctoption(correctoption1)
            correctoption2 = request.form["correctoption2"]
            quizzes.add_correctoption(correctoption2)
            correctoption3 = request.form["correctoption3"]
            quizzes.add_correctoption(correctoption3)
            correctoption4 = request.form["correctoption4"]
            quizzes.add_correctoption(correctoption4)
            correctoption5 = request.form["correctoption5"]
            quizzes.add_correctoption(correctoption5)
            return redirect("/admin")

@app.route("/quizremoved", methods=["GET", "POST"])
def quizremoved():
    if request.method == "GET":
        return render_template("quizremoved.html")
    else:
        remove_quiz = request.form["quizremove"]
        quizname = request.form["quiz_id"]
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        else:
            if remove_quiz:
                quizzes.delete_quiz_id(quizname)
                return render_template("quizremoved.html", quizname=quizname)

@app.route("/rating/<int:quiz_id>", methods=["GET", "POST"])
def rating(quiz_id):
    if request.method == "GET":
        return render_template("rating.html")
    else:
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        else:
            username = session["username"]
            if not users.check_ifrated(quiz_id, username):
                rating = request.form["rating"]
                username = request.form["username"]
                print(username)
                quizzes.save_rating(quiz_id, rating, username)
                message = f"Success!"
                added = f" added"
                ratings = quizzes.calculate_ratings()
                leaderboard = users.calculate_leaderboard()
                return render_template("rating.html", added=added, message=message, ratings=ratings,
                                       leaderboard=leaderboard)
            else:
                error = f"You have already rated this quiz."
                not_added = f" not added"
                ratings = quizzes.calculate_ratings()
                leaderboard = users.calculate_leaderboard()
                return render_template("rating.html", not_added=not_added, error=error, ratings=ratings,
                                       leaderboard=leaderboard)

@app.route("/search")
def search():
    if request.method == "GET":
        category = request.args.get("category")
        result = quizzes.show_published_quizzes_category(category)
        leaderboard = users.calculate_leaderboard()
        ratings = quizzes.calculate_ratings()
        message = f"No search results in this category"
        return render_template("search.html", message=message, result=result, category=category,
                               leaderboard=leaderboard, ratings=ratings)
    else:
        return redirect("/")
