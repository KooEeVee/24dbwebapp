from db import db
from flask import session
from sqlalchemy import text
from werkzeug.security import check_password_hash, generate_password_hash
    
def create_user(username):
    try:
        sql = text("INSERT INTO users (username) VALUES (:username)")
        db.session.execute(sql, {"username":username})
        db.session.commit()
        return True    
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def check_username(username):
    try:
        sql = text("SELECT EXISTS(SELECT 1 FROM users WHERE username=:username)")
        result = db.session.execute(sql, {"username":username})
        exists = result.fetchone()[0]
        return exists
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def register(username, password, admin, gdpr):
    h_password = generate_password_hash(password)
    try:
        sql = text("UPDATE users SET password=:h_password, user_admin=:admin, gdpr=:gdpr WHERE username=:username")
        db.session.execute(sql, {"username":username, "h_password":h_password, "gdpr":gdpr, "admin":admin})
        db.session.commit()
        return True    
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def login(username, password):
    try:
        sql = text("SELECT * FROM users WHERE username=:username")
        result = db.session.execute(sql, {"username":username})
        user = result.fetchone()
        role = user[3]
        print(role)
        if check_password_hash(user[2], password):
            session["username"] = username
            session["role"] = role
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def check_ifadmin(username):
    try:
        sql = text("SELECT * FROM users WHERE username=:username")
        result = db.session.execute(sql, {"username":username})
        user = result.fetchone()
        if user[3]=="admin":
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def check_ifplayed(quiz_id, username):
    try:
        sql = text("SELECT EXISTS(SELECT 1 FROM answers WHERE username=:username AND quiz_id=:quiz_id)")
        result = db.session.execute(sql, {"username":username, "quiz_id":quiz_id})
        played = result.fetchone()[0]
        return played
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def calculate_correctanswers(username):
    try:
        sql = text("""SELECT answers.username, COUNT(*) AS correct_answer_count FROM answers 
                   LEFT JOIN options ON answers.option_id = options.id
                   WHERE answers.username=:username AND options.correct_option =:correct_option
                   GROUP BY answers.username""")
        result = db.session.execute(sql, {"username":username, "correct_option":True})
        stats = result.fetchall()
        return stats
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def calculate_playedquizzes(username):
    try:
        sql = text("""SELECT answers.quiz_id, COUNT(DISTINCT quiz_id) AS played_quizzes_count FROM answers
                   WHERE answers.username=:username
                   GROUP BY answers.quiz_id""")
        result = db.session.execute(sql, {"username":username})
        stats = result.fetchall()
        return stats
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def calculate_leaderboard():
    try:
        sql = text("""SELECT users.username, COUNT(answers.id) AS correct_answer_count, DENSE_RANK() OVER (ORDER BY COUNT(answers.id) DESC) AS rank
                   FROM users
                   LEFT JOIN answers ON users.username = answers.username
                   LEFT JOIN options ON answers.option_id = options.id
                   WHERE options.correct_option =:correct_option AND answers.username != 'guest'
                   GROUP BY users.username
                   ORDER BY rank""")
        result = db.session.execute(sql, {"correct_option":True})
        stats = result.fetchall()
        return stats
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def calculate_playedquizzes_created(username):
    try:
        sql = text("""SELECT quizzes.created_by, quizzes.quiz_label, COUNT(answers.quiz_id) AS played_quizzes_count FROM answers
                   LEFT JOIN quizzes ON quizzes.id = answers.quiz_id
                   WHERE quizzes.created_by=:username
                   GROUP BY quizzes.quiz_label, quizzes.created_by""")
        result = db.session.execute(sql, {"username":username})
        stats = result.fetchall()
        return stats
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def calculate_correctanswers_created(username):
    try:
        sql = text("""SELECT quizzes.created_by, quizzes.quiz_label, COUNT(answers.id) AS correct_answer_count FROM answers 
                   LEFT JOIN options ON answers.option_id = options.id
                   LEFT JOIN quizzes ON answers.quiz_id = quizzes.id
                   WHERE quizzes.created_by=:username AND options.correct_option =:correct_option
                   GROUP BY quizzes.created_by, quizzes.quiz_label""")
        result = db.session.execute(sql, {"username":username, "correct_option":True})
        stats = result.fetchall()
        return stats
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def calculate_allanswers_created(username):
    try:
        sql = text("""SELECT quizzes.created_by, quizzes.quiz_label, COUNT(*) AS all_answer_count FROM answers 
                   LEFT JOIN quizzes ON answers.quiz_id = quizzes.id
                   WHERE quizzes.created_by=:username
                   GROUP BY quizzes.created_by, quizzes.quiz_label""")
        result = db.session.execute(sql, {"username":username})
        stats = result.fetchall()
        return stats
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

