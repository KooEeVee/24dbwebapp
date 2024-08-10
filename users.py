from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

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