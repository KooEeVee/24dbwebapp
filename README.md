# Music Quiz Platform

## Välipalautus 3 18.8.2024

The app is mostly ready. All the features are listed below and marked if done. UI, design, security and privacy need more attention before the final version.

How to test the app locally:

1. Clone the repository to your computer
2. Go to the root directory and create .env file with your DATABASE_URL= and SECRET_KEY=
3. Activate venv and install recuirements
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r ./requirements.txt
4. Create tables
    $ psql < schema.sql
5. OPTIONAL: Test data is available in quizzes.sql file. 4 test users and 2 test quizzes are provided, if you wish to use them. Note! Login password check is disabled, so that the test data login works. Final version will have password check enabled.
    $ psql < quizzes.sql
6. Run the app
    $ flask run


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
- As anyone, see lists of available quizzes sorted by their tags
- As anyone, take a quiz and solve tasks
- As anyone, see the ranking lists of registered users
- As a user or admin, create or remove an account
- As a user or admin, log in and out
- As a user, see the results and rankings of own finished quizzes
- As a user, rate the quiz
- As an admin, create new quizzes, remove quizzes
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
* [x]... and many more

Create a user account, log in and log out, remove account, stats
* [x]users.py: [x]register user (username, password, admin or user, gdpr check, created at), [x]login, [x]logout, [x]session, [x]hash password, [x]remove account and userdata, [x]creating the ranking list, [x]showing the ranking list, [x]creating the user stats, [x]showing the user stats, [x]creating the admin stats, [x]showing the admin stats

Create and play a quiz
* [x]quizzes.py: [x]saving quizzes, questions, answer options and correct answers, [x]showing quizzes on admin page, [x]checking correct answers when a quiz is played, [x]returning the quiz result after playing, [x]showing quizzes on the front page, [x]tagging quizzes, [x]rating quizzes, [x]searching quizzes

Database
* [x]db.py: database connection launch
* [x]schema.sql

Other files
* [x].gitignore
* [x].env
* [x]requirements.txt
* [x]quizzes.sql (test data)

Layout and design (WIP)
* [x]layout.html
* [x]Bootstrap design
* Accessibility WIP

Security and privacy
* WIP

Misc tasks
* [x]Fix quiz answer validation
* [x]If user input is invalid, load the prefilled form
* []Show all relevant validation errors at the same time
* [x]Show only relevant navi items
* [x]Fix CSRF vulnerability
* [x]Fix double headers on user and admin pages
* [x]Fix quiz creation number of characters
* [x]Don't save the quiz, if questions and options are not set
* [x]Don't save the user, if password and admin/user are not set
* [x]Pylint
* [x]Fix user account remove
* [x]Fix published date
* [x]Questions must be unique in a quiz, validation needed
* [x]Eanble password check
* [x]List the played quizzes for users
* []Fix login with wrong username
