run:
	python app.py server

active:
	pipenv shell

requirements:
	pip freeze > requirements.txt

dependencies:
	pipenv sync
