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
    
def get_quizid(quizname):
    try:
        sql = text("SELECT id FROM quizzes WHERE label=:quizname")
        result = db.session.execute(sql, {"quizname":quizname})
        quizid = result.fetchone()[0]
        return quizid
    except:
        return False

def add_question(quizid, question):
    try:
        sql = text("INSERT INTO questions (quiz_id, label) VALUES (:quiz_id, :label)")
        db.session.execute(sql, {"quiz_id":quizid, "label":question})
        db.session.commit()
        return True    
    except:
        return False
    
def get_questionid(question):
    try:
        sql = text("SELECT id FROM questions WHERE label=:question")
        result = db.session.execute(sql, {"question":question})
        questionid = result.fetchone()[0]
        return questionid
    except:
        return False
    

def add_options(questionid, option):
    try:
        sql = text("INSERT INTO options (question_id, label) VALUES (:question_id, :label)")
        db.session.execute(sql, {"question_id":questionid, "label":option})
        db.session.commit()
        return True    
    except:
        return False
    
def get_optionid(option):
    try:
        sql = text("SELECT id FROM options WHERE label=:option")
        result = db.session.execute(sql, {"option":option})
        optionid = result.fetchone()[0]
        return optionid
    except:
        return False
    
def add_correctoption(optionid):
    try:
        sql = text("UPDATE options SET correct_option=:correctoption WHERE id=:optionid")
        db.session.execute(sql, {"optionid":optionid, "correctoption": True})
        db.session.commit()
        return True
    except:
        return False