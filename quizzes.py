from sqlalchemy import text
from db import db

def create_quiz(quizname, created_by):
    sql = text("INSERT INTO quizzes (quiz_label, created_by) VALUES (:quiz_label, :created_by)")
    db.session.execute(sql, {"quiz_label":quizname, "created_by":created_by})
    db.session.commit()

def check_quizname(quizname):
    sql = text("SELECT EXISTS(SELECT 1 FROM quizzes WHERE quiz_label=:quizname)")
    result = db.session.execute(sql, {"quizname":quizname})
    exists = result.fetchone()[0]
    return exists

def get_quizid(quizname):
    sql = text("SELECT id FROM quizzes WHERE quiz_label=:quizname")
    result = db.session.execute(sql, {"quizname":quizname})
    quizid = result.fetchone()[0]
    return quizid

def get_quizid_option(option_id):
    sql = text("""SELECT questions.quiz_id FROM questions
               LEFT JOIN options ON questions.id = options.question_id 
               WHERE options.id=:option_id""")
    result = db.session.execute(sql, {"option_id":option_id})
    quiz_id = result.fetchone()[0]
    return quiz_id

def get_quizname(quiz_id):
    sql = text("SELECT quiz_label FROM quizzes WHERE id=:quiz_id")
    result = db.session.execute(sql, {"quiz_id":quiz_id})
    quizname = result.fetchone()[0]
    return quizname

def get_published(quiz_id):
    sql = text("SELECT published FROM quizzes WHERE id=:quiz_id")
    result = db.session.execute(sql, {"quiz_id":quiz_id})
    published = result.fetchone()[0]
    return published

def get_published_at(quiz_id):
    sql = text("SELECT published_at FROM quizzes WHERE id=:quiz_id")
    result = db.session.execute(sql, {"quiz_id":quiz_id})
    published_at = result.fetchone()[0]
    return published_at

def get_questions(quiz_id):
    sql = text("""SELECT questions.question_label, questions.id FROM quizzes
               LEFT JOIN questions ON quizzes.id=questions.quiz_id
               WHERE quizzes.id=:quiz_id
               ORDER BY questions.id ASC""")
    result = db.session.execute(sql, {"quiz_id":quiz_id})
    questions = result.fetchall()
    return questions

def get_questionid(question, quiz_id):
    sql = text("SELECT id FROM questions WHERE question_label=:question AND quiz_id=:quiz_id")
    result = db.session.execute(sql, {"question":question, "quiz_id":quiz_id})
    questionid = result.fetchone()[0]
    return questionid

def get_questionid_option(option_id):
    sql = text("SELECT question_id FROM options WHERE id=:option_id")
    result = db.session.execute(sql, {"option_id":option_id})
    questionid = result.fetchone()[0]
    return questionid

def get_options(quiz_id, questionname):
    sql = text("""SELECT options.option_label, options.id FROM quizzes
               LEFT JOIN questions ON quizzes.id=questions.quiz_id 
               LEFT JOIN options ON questions.id=options.question_id
               WHERE quizzes.id=:quiz_id AND questions.question_label=:questionname
               ORDER BY options.id ASC""")
    result = db.session.execute(sql, {"quiz_id":quiz_id, "questionname":questionname})
    options = result.fetchall()
    return options

def get_optionid(option):
    sql = text("SELECT id FROM options WHERE option_label=:option")
    result = db.session.execute(sql, {"option":option})
    optionid = result.fetchone()[0]
    return optionid

def get_option(option_id):
    sql = text("SELECT option_label FROM options WHERE id=:option_id")
    result = db.session.execute(sql, {"option_id":option_id})
    option = result.fetchone()[0]
    return option

def check_ifcorrectoption(option_id):
    sql = text("SELECT correct_option FROM options WHERE id=:option_id")
    result = db.session.execute(sql, {"option_id":option_id})
    correct_option = result.fetchone()[0]
    return correct_option

def get_correctoption_label(question_id):
    sql = text("""SELECT option_label FROM options
               WHERE question_id=:question_id AND correct_option=:correct_option""")
    result = db.session.execute(sql, {"question_id":question_id, "correct_option":True})
    correct_option = result.fetchone()[0]
    return correct_option

def add_category(quiz_id, category):
    sql = text("UPDATE quizzes SET category=:category WHERE id=:quiz_id")
    db.session.execute(sql, {"category":category, "quiz_id":quiz_id})
    db.session.commit()

def add_question(quizid, question):
    sql = text("INSERT INTO questions (quiz_id, question_label) VALUES (:quiz_id, :question_label)")
    db.session.execute(sql, {"quiz_id":quizid, "question_label":question})
    db.session.commit()
    return True

def add_options(questionid, option):
    sql = text("""INSERT INTO options (question_id, option_label)
               VALUES (:question_id, :option_label)""")
    db.session.execute(sql, {"question_id":questionid, "option_label":option})
    db.session.commit()

def add_correctoption(optionid):
    sql = text("UPDATE options SET correct_option=:correctoption WHERE id=:optionid")
    db.session.execute(sql, {"optionid":optionid, "correctoption": True})
    db.session.commit()

def show_quizzes_toadmin(username):
    sql = text("""SELECT quizzes.quiz_label, quizzes.published,
               quizzes.published_at, quizzes.category,
               questions.quiz_id, questions.question_label, 
               options.question_id, options.option_label, options.correct_option,
               options.id
               FROM quizzes 
               LEFT JOIN questions ON quizzes.id=questions.quiz_id 
               LEFT JOIN options ON questions.id=options.question_id 
               WHERE quizzes.created_by=:username
               ORDER BY quizzes.published_at DESC, options.question_id ASC,
               options.id ASC""")
    result = db.session.execute(sql, {"username":username})
    list_quizzes = result.fetchall()
    dict_quizzes = {}
    for row in list_quizzes:
        quiz_label = row.quiz_label
        if quiz_label not in dict_quizzes:
            dict_quizzes[quiz_label] = {
                "published": row.published,
                "quiz_id": row.quiz_id,
                "published_at": row.published_at,
                "category": row.category,
                "questions": {}
            }
        question_label = row.question_label
        if question_label not in dict_quizzes[quiz_label]["questions"]:
            dict_quizzes[quiz_label]["questions"][question_label] = {
                "question_id": row.question_id,
                "options": []
            }
        optionlist = {
            "option_label": row.option_label,
            "correct_option": row.correct_option
        }
        dict_quizzes[quiz_label]["questions"][question_label]["options"].append(optionlist)
    return dict_quizzes

def publish_quiz(quiz_id, published):
    sql = text("UPDATE quizzes SET published=:published, published_at=NOW() WHERE id=:quiz_id")
    db.session.execute(sql, {"quiz_id":quiz_id, "published": published})
    db.session.commit()
    return True

def show_published_quizzes():
    sql = text("""SELECT id, quiz_label, created_by, category FROM quizzes
               WHERE published=:published""")
    result = db.session.execute(sql, {"published":True})
    list_quizzes = result.fetchall()
    return list_quizzes

def show_published_quizzes_category(category):
    sql = text("""SELECT id, quiz_label, created_by, category FROM quizzes
               WHERE published=:published AND category=:category""")
    result = db.session.execute(sql, {"published":True, "category":category})
    list_quizzes = result.fetchall()
    return list_quizzes

def show_quiz_tousers(quiz_id):
    sql = text("""SELECT quizzes.quiz_label, quizzes.published,
               questions.quiz_id, questions.question_label, 
               options.question_id, options.option_label, options.correct_option
               FROM quizzes
               LEFT JOIN questions ON quizzes.id=questions.quiz_id
               LEFT JOIN options ON questions.id=options.question_id
               WHERE quizzes.id=:quiz_id""")
    result = db.session.execute(sql, {"quiz_id":quiz_id})
    list_quizzes = result.fetchall()
    dict_quizzes = {}
    for row in list_quizzes:
        quiz_label = row.quiz_label
        if quiz_label not in dict_quizzes:
            dict_quizzes[quiz_label] = {
                "published": row.published,
                "quiz_id": row.quiz_id,
                "questions": {}
            }
        question_label = row.question_label
        if question_label not in dict_quizzes[quiz_label]["questions"]:
            dict_quizzes[quiz_label]["questions"][question_label] = {
                "question_id": row.question_id,
                "options": []
            }
        optionlist = {
            "option_label": row.option_label,
            "correct_option": row.correct_option
        }
        dict_quizzes[quiz_label]["questions"][question_label]["options"].append(optionlist)
    return dict_quizzes

def save_answer(username, option_id, quiz_id):
    sql = text("""INSERT INTO answers (username, option_id, quiz_id)
               VALUES (:username, :option_id, :quiz_id)""")
    db.session.execute(sql, {"username":username, "option_id":option_id, "quiz_id":quiz_id})
    db.session.commit()

def save_rating(quiz_id, rating, username):
    sql = text("INSERT INTO ratings (quiz_id, rating, username) VALUES (:quiz_id, :rating, :username)")
    db.session.execute(sql, {"quiz_id":quiz_id, "rating":rating, "username":username})
    db.session.commit()

def calculate_ratings():
    sql = text("""SELECT ratings.quiz_id, quizzes.quiz_label,
               COUNT(CASE WHEN ratings.rating = 'meh' THEN 1 END) AS meh_count,
               COUNT(CASE WHEN ratings.rating = 'nice' THEN 1 END) AS nice_count,
               COUNT(CASE WHEN ratings.rating = 'diamond' THEN 1 END) AS diamond_count,
               COUNT(*) AS total_ratings_count
               FROM ratings
               LEFT JOIN quizzes ON ratings.quiz_id = quizzes.id
               GROUP BY ratings.quiz_id, quizzes.quiz_label""")
    result = db.session.execute(sql)
    stats = result.fetchall()
    return stats

def delete_answer(username):
    sql = text("DELETE FROM answers WHERE username=:username")
    db.session.execute(sql, {"username":username})
    db.session.commit()

def delete_quiz(username):
    sql = text("DELETE FROM quizzes WHERE created_by=:username")
    db.session.execute(sql, {"username":username})
    db.session.commit()

def delete_quiz_id(quizname):
    sql = text("DELETE FROM quizzes WHERE quiz_label=:quizname")
    db.session.execute(sql, {"quizname":quizname})
    db.session.commit()

def delete_rating(username):
    sql = text("DELETE FROM ratings WHERE username=:username")
    db.session.execute(sql, {"username":username})
    db.session.commit()

    