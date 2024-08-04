# Music Quiz Platform

## Overview

Music Quiz Platform offers users a fun place to refresh and test music related skills and knowledge. Admins can easily create multiple simple quizzes. No need for user registration, but registered users can see their stats and be placed on ranking lists.

## Features

- As anyone, see a list of available quizzes and their ratings
- As anyone, see lists of available quizzes sorted by their ratings and tags
- As anyone, search a quiz by tags
- As anyone, take a quiz and solve tasks (text, audio?)
- As anyone, see the ranking lists of registered users
- As a user or admin, create or remove an account
- As a user or admin, log in and out
- As a user, see the results and rankings of own finished quizzes
- As a user, rate the quiz
- As an admin, create new quizzes, edit and remove if not published
- As an admin, create new tasks (text, audio?) in quizzes, edit and remove if not published
- As an admin, tag quizzes
- As an admin, see a list of your own unpublished and published quizzes
- As an admin, see the stats of your quizzes: how many users, results

## To-do

Routes and app
* [x]routes.py: functions for page requests
* [x]app.py: application launch

Templates
* [x]index.html
* [x]login.html
* [x]register.html
* [x]logout.html
* [x]user.html
* [x]admin.html
* [x]accountremoved.html
* [x]quiz.html
* [x]quizresult.html

Create a user account, log in and log out, remove account
* []users.py: []register user (username, password), []login, []logout, []session, []hash password, []username and []password validation rules, []remove account and userdata

Creating and playing a quiz
* [x]quizzes.py: []saving quizzes, questions, answer options and correct answers, []checking correct answers when a quiz is played, []returning the quiz result after playing

Database
* [x]db.py: database connection launch
* [x]schema.sql

Other files
* [x].gitignore
* [x].env
* []requirements.txt

Layout
* Bootstrap template
* [x]layout.html

Security and privacy
* WIP