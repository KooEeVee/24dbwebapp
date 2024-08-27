import secrets
from flask import session
from sqlalchemy import text
from werkzeug.security import check_password_hash, generate_password_hash
from db import db

def create_user(username):
    sql = text("INSERT INTO users (username) VALUES (:username)")
    db.session.execute(sql, {"username":username})
    db.session.commit()

def check_username(username):
    sql = text("SELECT EXISTS(SELECT 1 FROM users WHERE username=:username)")
    result = db.session.execute(sql, {"username":username})
    exists = result.fetchone()[0]
    return exists

def register(username, password, admin, gdpr):
    h_password = generate_password_hash(password)
    sql = text("""UPDATE users SET password=:h_password, user_admin=:admin, gdpr=:gdpr
               WHERE username=:username""")
    db.session.execute(sql, {"username":username, "h_password":h_password, "gdpr":gdpr, "admin":admin})
    db.session.commit()

def login(username, password):
    sql = text("SELECT id, username, password, user_admin FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    print(user)
    if user is not None:
        role = user[3]
        if check_password_hash(user[2], password):
            session["username"] = username
            session["role"] = role
            session["csrf_token"] = secrets.token_hex(16)
            return True
        else:
            return False

def check_ifadmin(username):
    sql = text("SELECT id, username, password, user_admin FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user[3] == "admin":
        return True
    else:
        return False
    
def check_ifrated(quiz_id, username):
    sql = text("SELECT EXISTS(SELECT 1 FROM ratings WHERE username=:username AND quiz_id=:quiz_id)")
    result = db.session.execute(sql, {"username":username, "quiz_id":quiz_id})
    rated = result.fetchone()[0]
    return rated

def check_ifplayed(quiz_id, username):
    sql = text("SELECT EXISTS(SELECT 1 FROM answers WHERE username=:username AND quiz_id=:quiz_id)")
    result = db.session.execute(sql, {"username":username, "quiz_id":quiz_id})
    played = result.fetchone()[0]
    return played

def calculate_correctanswers(username):
    sql = text("""SELECT answers.username, COUNT(*) AS correct_answer_count FROM answers
                LEFT JOIN options ON answers.option_id = options.id
                WHERE answers.username=:username AND options.correct_option =:correct_option
                GROUP BY answers.username""")
    result = db.session.execute(sql, {"username":username, "correct_option":True})
    stats = result.fetchall()
    return stats

def calculate_playedquizzes(username):
    sql = text("""SELECT COUNT(DISTINCT answers.quiz_id) AS played_quizzes_count FROM answers
                WHERE answers.username=:username""")
    result = db.session.execute(sql, {"username":username})
    stats = result.fetchall()
    return stats

def show_playedquizzes(username):
    sql = text("""SELECT DISTINCT quiz_label FROM quizzes
                LEFT JOIN answers ON quizzes.id = answers.quiz_id 
                WHERE answers.username=:username""")
    result = db.session.execute(sql, {"username":username})
    quizzes = result.fetchall()
    return quizzes

def calculate_leaderboard():
    sql = text("""SELECT users.username, COUNT(answers.id) AS correct_answer_count,
               DENSE_RANK() OVER (ORDER BY COUNT(answers.id) DESC) AS rank
               FROM users
               LEFT JOIN answers ON users.username = answers.username
               LEFT JOIN options ON answers.option_id = options.id
               WHERE options.correct_option =:correct_option AND answers.username != 'guest'
               GROUP BY users.username
               ORDER BY rank""")
    result = db.session.execute(sql, {"correct_option":True})
    stats = result.fetchall()
    return stats

def calculate_playedquizzes_created(username):
    sql = text("""SELECT quizzes.created_by, quizzes.quiz_label,
               COUNT(answers.quiz_id) / 5 AS played_quizzes_count FROM answers
                LEFT JOIN quizzes ON quizzes.id = answers.quiz_id
                WHERE quizzes.created_by=:username
                GROUP BY quizzes.quiz_label, quizzes.created_by""")
    result = db.session.execute(sql, {"username":username})
    stats = result.fetchall()
    return stats

def calculate_correctanswers_created(username):
    sql = text("""SELECT quizzes.created_by, quizzes.quiz_label,
               COUNT(answers.id) AS correct_answer_count FROM answers 
                LEFT JOIN options ON answers.option_id = options.id
                LEFT JOIN quizzes ON answers.quiz_id = quizzes.id
                WHERE quizzes.created_by=:username AND options.correct_option =:correct_option
                GROUP BY quizzes.created_by, quizzes.quiz_label""")
    result = db.session.execute(sql, {"username":username, "correct_option":True})
    stats = result.fetchall()
    return stats

def calculate_allanswers_created(username):
    sql = text("""SELECT quizzes.created_by, quizzes.quiz_label,
               COUNT(*) AS all_answer_count FROM answers 
                LEFT JOIN quizzes ON answers.quiz_id = quizzes.id
                WHERE quizzes.created_by=:username
                GROUP BY quizzes.created_by, quizzes.quiz_label""")
    result = db.session.execute(sql, {"username":username})
    stats = result.fetchall()
    return stats

def remove_user(username):
    sql = text("DELETE FROM users WHERE username=:username")
    db.session.execute(sql, {"username":username})
    db.session.commit()
