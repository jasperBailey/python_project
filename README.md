# The Impractical Beep Boop Maker

This makes beeps and boops.

It's a webapp I made during a course at CodeClan which was required to contain **strictly no JavaScript**. With that in mind, I thought it would be a great idea to input MIDI notes using html forms and generate an mp3 file from there. It's locally hosted - to run it yourself you'll need to:

## Install dependencies

You should have Python 3.10+ installed: https://www.python.org/downloads/

(older versions might work but no guarantee)

You should have PostgreSQL installed: https://www.postgresql.org/download/

You should have the following packages installed:

`pip install flask`

`pip install jinja`
*This should come automatically with flask, so you may not need to do this one*

`pip install psycopg2`

`pip install pydub`

`pip install ffmpeg`

## Create the PostgreSQL database

Run these commands from the project directory.

`createdb track_manager` initialises the database
`psql db/track_manager.sql` creates the required tables 

## Populate it with the sample data (if you so desire)

`python3 console.py`

## Run the local server

`flask run`

Your practical music making application should now be running on localhost on the specified port.
