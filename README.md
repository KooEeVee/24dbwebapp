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
- As an admin, create new quizzes, remove quizzes
- As an admin, create new tasks in quizzes
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
* [x]users.py: [x]register user (username, password, admin or user, gdpr check, created at), [x]login, [x]logout, [x]session, [x]hash password, [x]remove account and userdata, [x]creating the ranking list, [x]showing the ranking list, [x]creating the user stats, [x]showing the user stats, [x]creating the admin stats, [x]showing the admin stats

Create and play a quiz (WIP)
* [x]quizzes.py: [x]saving quizzes, questions, answer options and correct answers, [x]showing quizzes on admin page, [x]checking correct answers when a quiz is played, [x]returning the quiz result after playing, [x]showing quizzes on the front page, [x]tagging quizzes, [x]rating quizzes, [x]searching quizzes

Database
* [x]db.py: database connection launch
* [x]schema.sql

Other files (WIP)
* [x].gitignore
* [x].env
* []requirements.txt

Layout and design (WIP)
* [x]layout.html
* Bootstrap
* Accessibility WIP

Security and privacy
* WIP

Misc tasks
* [x]Show menu items according to user login status
* [x]Guide the user after successful username check
* [x]20 character username
* [x]Internar Server Error if log out when not logged in
* [x]Guide user after successful quiz name check
* [x]Drop down menu or field check for correct options
* [x]Add publish quiz time stamp when quiz is published
* [x]Add remove quiz button
* [x]List quizzes newest first on admin page
* Fix question and option order when showing quizzes
* [x]Internal Server Error when playing as not loggedin
* [x]Loggedin users' answers are saved only once
* [x]Admin can't play own quiz
* [x]Add cancel buttons to forms
* [x]Message no quizzes yet on admin page
* [x]Add your answers to quiz result page
* [x]Messages according to the result on the result page
* [x]Add leaderboard to quiz and result page
* [x]Fix played quizzes counter
* [x]Fix save message on the quest result page
* [x]Fix admin answer stats
* [x]Only logged in users can rate quizzes