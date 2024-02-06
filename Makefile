requirements-generate:
	@echo "Generate requirements.txt file with hashes."
	poetry export -f requirements.txt --with=test --output requirements.txt

build-run-project:
	@echo "Running project with docker."
	docker-compose up --build

test:
	@echo "Running tests with pytest."
	docker-compose run onidata pytest -vvv

makemigrations:
	@echo "Running makemigrations with docker."
	docker-compose run onidata python3 manage.py makemigrations

migrate:
	@echo "Running migrate with docker."
	docker-compose run onidata python3 manage.py migrate

create-super-user:
	@echo "Creating superuser."
	docker-compose run onidata python3 manage.py createsuperuser

itsmine:
	@echo "Itsmine"
	sudo chown -R $USER src
