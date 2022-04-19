#Create a database schema (CREATE TABLE statementss) for this app
python3 manage.py makemigrations joesChops

#push the migration
python3 manage.py migrate

#migrate with database
python3 manage.py sqlmigrate joesChops 000x

#create admin account
python3 manage.py createsuperuser

#start the server
python3 manage.py runserver