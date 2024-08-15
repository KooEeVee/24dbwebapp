CREATE TABLE quizzes (
    id SERIAL PRIMARY KEY,
    quiz_label TEXT UNIQUE, 
    published BOOLEAN DEFAULT FALSE,
    created_by TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    published_at TIMESTAMP
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
    correct_option BOOLEAN DEFAULT FALSE
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    user_admin TEXT,
    gdpr TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    username TEXT,
    option_id INTEGER REFERENCES options,
    quiz_id INTEGER REFERENCES quizzes,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

