# Music Quiz Platform

## Lopullinen palautus 1.9.2024

How to test the app locally:

1. Clone the repository to your computer
2. Go to the root directory and create .env file with your DATABASE_URL= and SECRET_KEY=
3. Activate venv and install recuirements
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r ./requirements.txt
4. Create tables
    $ psql < schema.sql
5. OPTIONAL: Test data is available in quizzes.sql file. Two test quizzes are provided, if you wish to use them.
    $ psql < quizzes.sql
6. Run the app
    $ flask run

## Overview

Music Quiz Platform offers users a fun place to refresh and test music related skills and knowledge. Admins can easily create multiple simple quizzes. No need for user registration, but registered users can see their stats, rate quizzes and be placed on the leaderboard. Platform is suitable for small groups of people enjoying music quizzes, not designed for large scale use.

## Features

- As anyone, see available quizzes, all or sorted by their categories
- As anyone, play a quiz (admins can't play their own)
- As anyone, see the leaderboard of registered users and quiz ratings
- As a user or admin, create or remove an account
- As a user or admin, log in and out
- As a user or admin, see the results of own finished quizzes
- As a user or admin, rate a quiz (admins can't rate their own)
- As an admin, create new quizzes, remove quizzes
- As an admin, tag quizzes with categories
- As an admin, publish quizzes
- As an admin, see a list of own unpublished and published quizzes
- As an admin, see the stats of own quizzes: how many users, results