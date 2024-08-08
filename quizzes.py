from db import db
from sqlalchemy import text

def create_quiz(quizname):
    try:
        sql = text("INSERT INTO quizzes (quiz_label, published) VALUES (:quiz_label, :published)")
        db.session.execute(sql, {"quiz_label":quizname, "published":False})
        db.session.commit()
        return True    
    except:
        return False
    
def get_quizid(quizname):
    try:
        sql = text("SELECT id FROM quizzes WHERE quiz_label=:quizname")
        result = db.session.execute(sql, {"quizname":quizname})
        quizid = result.fetchone()[0]
        return quizid
    except:
        return False

def add_question(quizid, question):
    try:
        sql = text("INSERT INTO questions (quiz_id, question_label) VALUES (:quiz_id, :question_label)")
        db.session.execute(sql, {"quiz_id":quizid, "question_label":question})
        db.session.commit()
        return True    
    except:
        return False
    
def get_questionid(question):
    try:
        sql = text("SELECT id FROM questions WHERE question_label=:question")
        result = db.session.execute(sql, {"question":question})
        questionid = result.fetchone()[0]
        return questionid
    except:
        return False
    

def add_options(questionid, option):
    try:
        sql = text("INSERT INTO options (question_id, option_label) VALUES (:question_id, :option_label)")
        db.session.execute(sql, {"question_id":questionid, "option_label":option})
        db.session.commit()
        return True    
    except:
        return False
    
def get_optionid(option):
    try:
        sql = text("SELECT id FROM options WHERE option_label=:option")
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
    
""" def show_quizzes_toadmin():
    try:
        sql = text("SELECT id, label, published FROM quizzes")
        result = db.session.execute(sql)
        list_quizzes = result.fetchall()
        return list_quizzes
    except:
        return False """
    
def show_quizzes_toadmin():
    try:
        sql = text("""SELECT quizzes.id, quizzes.quiz_label, quizzes.published, questions.question_label, options.option_label, correct_option 
                   FROM quizzes 
                   LEFT JOIN questions ON quizzes.id=questions.quiz_id 
                   LEFT JOIN options ON questions.id=options.question_id 
                   WHERE quizzes.id=32""")
        result = db.session.execute(sql)
        list_quizzes = result.fetchall()
        return list_quizzes
    except:
        return False
