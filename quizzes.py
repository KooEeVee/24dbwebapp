from db import db
from sqlalchemy import text

def create_quiz(quizname):
    try:
        sql = text("INSERT INTO quizzes (label, published) VALUES (:label, :published)")
        db.session.execute(sql, {"label":quizname, "published":False})
        db.session.commit()
        return True    
    except:
        return False
