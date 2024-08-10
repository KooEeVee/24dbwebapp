CREATE TABLE quizzes (
    id SERIAL PRIMARY KEY,
    quiz_label TEXT UNIQUE, 
    published BOOLEAN
);

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    quiz_id INTEGER REFERENCES quizzes,
    question_label TEXT
);

CREATE TABLE options (
    id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES questions,
    option_label TEXT,
    correct_option BOOLEAN
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    user_admin TEXT,
    gdpr TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
