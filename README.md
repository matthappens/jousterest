# jousterest
How to : 

1. Unzip the tar I'll have emailed you
2. If necessary set up the virtualenv, and install dependencies using 
> pip install -r requirements.txt
3. python manage.py runserver
4. the credentials are:
> username: jousterest_user
> password: jousterest
5. DB items are stored in the db.sqlite3 file

# notes
1. Normally I'd provide unit tests.  However in this case, there is not much beyond basic Django functionality and I was pressed for time.  Unit testing with tools like nose and Django's built in unit test framework is part of my daily activities and I'm a believer in TDD.  If you'd like me to provide tests, let me know.
2. I'd prefer an ajax style site, but based on the requirements it didn't sound like there'd be much chance to install additional python dependencies like django-rest framework
