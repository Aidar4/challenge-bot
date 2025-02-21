
lock:
	pip-compile --generate-hashes --no-emit-index-url --allow-unsafe

install:
	pip-sync requirements.txt --pip-args '--no-deps'

build:
	git pull
	docker-compose build bot_schedule

release:
	make build
	docker-compose stop bot_schedule
	docker-compose up -d bot_schedule
