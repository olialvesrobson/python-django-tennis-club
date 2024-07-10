
.PHONY: venv activate

_venv:
	python3.12 -m venv myenv

activate:
	source myenv/bin/activate

server:
	python manage.py runserver

migrate-server:
	python manage.py migrate && python manage.py runserver

worker:
	python -m celery -A project_name worker --loglevel info

beat:
	python -m celery -A project_name beat --loglevel info

shell:
	python manage.py shell

migrations:
	python manage.py makemigrations ${models}
	python manage.py migrate