runserver:
	python3 manage.py runserver --settings=settings.local

migrate:
	python3 manage.py migrate --settings=settings.local

makemigrations:
	python3 manage.py makemigrations --settings=settings.local

createsuperuser:
	python3 manage.py createsuperuser --settings=settings.local


runserver-prod:
	python3 manage.py runserver --settings=settings.prod