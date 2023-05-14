.PHONY: install migrate makemigrations runserver superuser update

install:
	poetry install
	
migrate:
	poetry run python3 -m core.manage migrate

makemigrations:
	poetry run python3 -m core.manage makemigrations

runserver:
	poetry run python3 -m core.manage runserver

superuser:
	poetry run python3 -m core.manage createsuperuser

startapp:
	poetry run python3 -m core.manage startapp $(name) $(path)

shell:
	poetry run python3 -m core.manage shell

update: install migrate ; @echo "Update complete!"


