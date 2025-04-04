runserver:
	python3 manage.py runserver --settings=settings.local

migrate:
	python3 manage.py migrate --settings=settings.local

makemigrations:
	python3 manage.py makemigrations --settings=settings.local

createsuperuser:
	python3 manage.py createsuperuser --settings=settings.local

shell:
	python3 manage.py shell --settings=settings.local

runserver-prod:
	python3 manage.py runserver --settings=settings.prod

# call with make copy-db -e DB_FILE=<your-file-name>
copy-db:
	mysqldump -u root amigurumis_db > $(DB_FILE)

create-local-db:
	echo "CREATE DATABASE amigurumi_db;" | mysql -u root

clear-local-db:
	echo "DROP DATABASE IF EXISTS amigurumis_db; CREATE DATABASE amigurumis_db;" | mysql -u root

# call with make import-db -e DB_FILE=<your-file-name>
import-db: clear-local-db
	mysql -u root amigurumis_db < $(DB_FILE)