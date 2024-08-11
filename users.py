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
    print(username, password, admin, gdpr)
    print(h_password)
    try:
        sql = "INSERT INTO users (username, password, admin, gdpr) VALUES (:username, :password, :admin, :gdpr)"
        db.session.execute(sql, {"username":username, "password":h_password, "admin":admin, "gdpr":gdpr})
        db.session.commit()
        return True
    except:
        return False