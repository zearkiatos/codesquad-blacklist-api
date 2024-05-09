activate:
	source run.sh; activate

install:
	pip install -r requirements.txt

run:
	source run.sh; run $(port)

docker-up:
	source run.sh; docker_up

docker-down:
	source run.sh; docker_down

docker-dev-up:
	docker compose -f=docker-compose.develop.yml up --build

docker-dev-down:
	docker compose -f=docker-compose.develop.yml down


run-docker:
ifeq ($(strip $(port)),)
	flask run -h 0.0.0.0
else
	flask run -p $(port) -h 0.0.0.0
endif

test:
	FLASK_ENV=test python -m unittest discover tests

docker-gunicorn:
	gunicorn --bind 0.0.0.0:5000 wsgi:application