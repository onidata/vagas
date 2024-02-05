requirements-generate:
	@echo "Generate requirements.txt file with hashes."
	poetry export -f requirements.txt --with=test --output requirements.txt

build:
	@echo "Running project with docker."
	docker-compose up --build

test:
	@echo "Running tests with pytest."
	docker-compose run onidata pytest -vvv
