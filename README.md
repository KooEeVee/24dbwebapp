# Music Quiz Platform

## Välipalautus 2

A very basic prototype of UI implemented. Most of the pages created and available for testing. Most of the forms created and available for testing. Note that any data (user accounts, quiz answers etc.) is not saved and any validation logic is not implemented, for example to check the quiz answers. None of the text content or layout design is final.

Navigation is available, but here's a list of pages:
* /
* /register
* /login
* /logout
* /admin
* /user
* /accountremoved
* /quiz
* /quizresult
* /newquiz

No need for creating any databases, installing flask should be enough to run the app locally and test the UI.

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
* [x]newquiz.html

Create a user account, log in and log out, remove account (WIP)
* []users.py: []register user (username, password), []login, []logout, []session, []hash password, []username and []password validation rules, []remove account and userdata

Create and play a quiz (WIP)
* [x]quizzes.py: []saving quizzes, questions, answer options and correct answers, []checking correct answers when a quiz is played, []returning the quiz result after playing, []showing quizzes on the front page, []tagging and rating the quizzes, []searching quizzes

Stats and ranking lists (WIP)
* []stats.py: []creating the ranking lists, []showing the ranking lists, []creating the stats, []showing the stats

Database (WIP)
* [x]db.py: database connection launch
* [x]schema.sql

Other files
* [x].gitignore
* [x].env
* []requirements.txt

Layout and design (WIP)
* [x]layout.html
* Bootstrap
* Accessibility WIP

Security and privacy
* WIP