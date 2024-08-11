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
    except:
        return False

def check_username(username):
    try:
        sql = text("SELECT EXISTS(SELECT 1 FROM users WHERE username=:username)")
        result = db.session.execute(sql, {"username":username})
        exists = result.fetchone()[0]
        return exists
    except:
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
        print(user[2])
        if check_password_hash(user[2], password):
            session["username"] = username
            return True
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
