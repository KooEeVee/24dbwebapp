from db import db
from sqlalchemy import text


def create_quiz(quizname, created_by):
    try:
        sql = text("INSERT INTO quizzes (quiz_label, created_by) VALUES (:quiz_label, :created_by)")
        db.session.execute(sql, {"quiz_label":quizname, "created_by":created_by})
        db.session.commit()
        return True    
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def check_quizname(quizname):
    try:
        sql = text("SELECT EXISTS(SELECT 1 FROM quizzes WHERE quiz_label=:quizname)")
        result = db.session.execute(sql, {"quizname":quizname})
        exists = result.fetchone()[0]
        return exists
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def get_quizid(quizname):
    try:
        sql = text("SELECT id FROM quizzes WHERE quiz_label=:quizname")
        result = db.session.execute(sql, {"quizname":quizname})
        quizid = result.fetchone()[0]
        return quizid
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def get_quizid_option(option_id):
    try:
        sql = text("SELECT questions.quiz_id FROM questions LEFT JOIN options ON questions.id = options.questionn_id WHERE options.id=:option_id")
        result = db.session.execute(sql, {"option_id":option_id})
        quiz_id = result.fetchone()[0]
        return quiz_id
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
    
def get_quizname(quiz_id):
    try:
        sql = text("SELECT quiz_label FROM quizzes WHERE id=:quiz_id")
        result = db.session.execute(sql, {"quiz_id":quiz_id})
        quizname = result.fetchone()[0]
        return quizname
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def get_published(quiz_id):
    try:
        sql = text("SELECT published FROM quizzes WHERE id=:quiz_id")
        result = db.session.execute(sql, {"quiz_id":quiz_id})
        published = result.fetchone()[0]
        return published
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def get_published_at(quiz_id):
    try:
        sql = text("SELECT published_at FROM quizzes WHERE id=:quiz_id")
        result = db.session.execute(sql, {"quiz_id":quiz_id})
        published_at = result.fetchone()[0]
        return published_at
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def get_questions(quiz_id):
    try:
        sql = text("""SELECT questions.question_label FROM quizzes 
                   LEFT JOIN questions ON quizzes.id=questions.quiz_id 
                   WHERE quizzes.id=:quiz_id""")
        result = db.session.execute(sql, {"quiz_id":quiz_id})
        questions = result.fetchall()
        return questions
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def get_questionid(question):
    try:
        sql = text("SELECT id FROM questions WHERE question_label=:question")
        result = db.session.execute(sql, {"question":question})
        questionid = result.fetchone()[0]
        return questionid
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def get_questionid_option(option_id):
    try:
        sql = text("SELECT question_id FROM options WHERE id=:option_id")
        result = db.session.execute(sql, {"option_id":option_id})
        questionid = result.fetchone()[0]
        return questionid
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def get_options(quiz_id, questionname):
    try:
        sql = text("""SELECT options.option_label, options.id FROM quizzes 
                   LEFT JOIN questions ON quizzes.id=questions.quiz_id 
                   LEFT JOIN options ON questions.id=options.question_id 
                   WHERE quizzes.id=:quiz_id AND questions.question_label=:questionname""")
        result = db.session.execute(sql, {"quiz_id":quiz_id, "questionname":questionname})
        options = result.fetchall()
        return options
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def get_optionid(option):
    try:
        sql = text("SELECT id FROM options WHERE option_label=:option")
        result = db.session.execute(sql, {"option":option})
        optionid = result.fetchone()[0]
        return optionid
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def check_ifcorrectoption(option_id):
    try:
        sql = text("SELECT correct_option FROM options WHERE id=:option_id")
        result = db.session.execute(sql, {"option_id":option_id})
        correct_option = result.fetchone()[0]
        return correct_option
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def get_correctoption_label(question_id):
    try:
        sql = text("SELECT option_label FROM options WHERE question_id=:question_id AND correct_option=:correct_option")
        result = db.session.execute(sql, {"question_id":question_id, "correct_option":True})
        correct_option = result.fetchone()[0]
        return correct_option
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def add_question(quizid, question):
    try:
        sql = text("INSERT INTO questions (quiz_id, question_label) VALUES (:quiz_id, :question_label)")
        db.session.execute(sql, {"quiz_id":quizid, "question_label":question})
        db.session.commit()
        return True    
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def add_options(questionid, option):
    try:
        sql = text("INSERT INTO options (question_id, option_label) VALUES (:question_id, :option_label)")
        db.session.execute(sql, {"question_id":questionid, "option_label":option})
        db.session.commit()
        return True    
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def add_correctoption(optionid):
    try:
        sql = text("UPDATE options SET correct_option=:correctoption WHERE id=:optionid")
        db.session.execute(sql, {"optionid":optionid, "correctoption": True})
        db.session.commit()
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
""" def show_quizname_toadmin():
    try:
        sql = text("SELECT id, label, published FROM quizzes")
        result = db.session.execute(sql)
        list_quizzes = result.fetchall()
        return list_quizzes
    except:
        return False """
    

def show_quizzes_toadmin(username):
    try:
        sql = text("""SELECT quizzes.quiz_label, quizzes.published, quizzes.published_at, questions.quiz_id, questions.question_label, options.question_id, options.option_label 
                   FROM quizzes 
                   LEFT JOIN questions ON quizzes.id=questions.quiz_id 
                   LEFT JOIN options ON questions.id=options.question_id 
                   WHERE quizzes.created_by=:username
                   ORDER BY quizzes.published_at DESC""")
        result = db.session.execute(sql, {"username":username})
        list_quizzes = result.fetchall()
        #print(list_quizzes)
        dict_quizzes = {}
        for row in list_quizzes:
            quiz_label = row.quiz_label
            #print(quiz_label)
            if quiz_label not in dict_quizzes:
                dict_quizzes[quiz_label] = {
                    "published": row.published,
                    "quiz_id": row.quiz_id,
                    "published_at": row.published_at,
                    "questions": {}
                }
            #print(dict_quizzes[quiz_label])
            question_label = row.question_label
            #print(question_label)
            if question_label not in dict_quizzes[quiz_label]["questions"]:
                dict_quizzes[quiz_label]["questions"][question_label] = {
                    "question_id": row.question_id,
                    "options": []
                }
            #print(dict_quizzes[quiz_label]["questions"][question_label])
            optionlist = {
                "option_label": row.option_label
            }
            dict_quizzes[quiz_label]["questions"][question_label]["options"].append(optionlist)
            #print(dict_quizzes)
        return dict_quizzes
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def show_questions_options(quiz_id):
    try:
        sql = text("""SELECT questions.quiz_id, questions.question_label, options.question_id, options.option_label 
                   FROM questions
                   LEFT JOIN options ON questions.id=options.question_id 
                   WHERE questions.quiz_id=:quiz_id""")
        result = db.session.execute(sql, {"quiz_id":quiz_id})
        list_questions = result.fetchall()
        #print(list_quizzes)
        dict_questions = {}
        for row in list_questions:
            question_label = row.question_label
            #print(quiz_label)
            if question_label not in dict_questions:
                dict_questions[question_label] = {
                    "question_id": row.question_id,
                    "options": []
                }
            optionlist = {
                "option_label": row.option_label
            }
            dict_questions[question_label]["options"].append(optionlist)
            #print(dict_quizzes)
        return dict_questions
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def publish_quiz(quiz_id, published):
    try:
        sql = text("UPDATE quizzes SET published=:published, published_at=NOW() WHERE id=:quiz_id")
        db.session.execute(sql, {"quiz_id":quiz_id, "published": published})
        db.session.commit()
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def show_published_quizzes():
    try:
        sql = text("SELECT id, quiz_label, created_by FROM quizzes WHERE published=:published")
        result = db.session.execute(sql, {"published":True})
        list_quizzes = result.fetchall()
        return list_quizzes
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def show_quiz_tousers(quiz_id):
    try:
        sql = text("""SELECT quizzes.quiz_label, quizzes.published, questions.quiz_id, questions.question_label, options.question_id, options.option_label, options.correct_option 
                   FROM quizzes 
                   LEFT JOIN questions ON quizzes.id=questions.quiz_id 
                   LEFT JOIN options ON questions.id=options.question_id 
                   WHERE quizzes.id=:quiz_id""")
        result = db.session.execute(sql, {"quiz_id":quiz_id})
        list_quizzes = result.fetchall()
        #print(list_quizzes)
        dict_quizzes = {}
        for row in list_quizzes:
            quiz_label = row.quiz_label
            #print(quiz_label)
            if quiz_label not in dict_quizzes:
                dict_quizzes[quiz_label] = {
                    "published": row.published,
                    "quiz_id": row.quiz_id,
                    "questions": {}
                }
            #print(dict_quizzes[quiz_label])
            question_label = row.question_label
            #print(question_label)
            if question_label not in dict_quizzes[quiz_label]["questions"]:
                dict_quizzes[quiz_label]["questions"][question_label] = {
                    "question_id": row.question_id,
                    "options": []
                }
            #print(dict_quizzes[quiz_label]["questions"][question_label])
            optionlist = {
                "option_label": row.option_label,
                "correct_option": row.correct_option
            }
            dict_quizzes[quiz_label]["questions"][question_label]["options"].append(optionlist)
            #print(dict_quizzes)
        return dict_quizzes
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def save_answer(username, option_id, quiz_id):
    try:
        sql = text("INSERT INTO answers (username, option_id, quiz_id) VALUES (:username, :option_id, :quiz_id)")
        db.session.execute(sql, {"username":username, "option_id":option_id, "quiz_id":quiz_id})
        db.session.commit()
        return True    
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
