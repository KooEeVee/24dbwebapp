CREATE TABLE quizzes (
    id SERIAL PRIMARY KEY,
    label TEXT,
    published BOOLEAN
);

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    quiz_id INTEGER REFERENCES quizzes,
    label TEXT
);

CREATE TABLE options (
    id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES questions,
    label TEXT,
    correct_option BOOLEAN
);

