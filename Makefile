.PHONY:
ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
COMPOSE_DIR:=$(ROOT_DIR)
DOCKER_COMPOSE := docker-compose
DOCKER_COMPOSE_FILE := $(COMPOSE_DIR)/docker-compose.yml

f ?= $(DOCKER_COMPOSE_FILE)
DOCKER_COMPOSE_FILE := $(f)

confirm:
	@( read -p "$(RED)Are you sure? [y/N]$(RESET): " sure && case "$$sure" in [yY]) true;; *) false;; esac )

check_env:
ifeq ("$(wildcard .env)","")
	cp env.sample .env
endif


start: ## Start all or c=<name> containers in FOREGROUND
	@$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) up $(c)

serve: ## Start all or c=<name> containers in BACKGROUND
	@$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) up $(c) -d

stop: ## Stop all or c=<name> containers
	@$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) stop $(c)

restart: ## Restart all or c=<name> containers
	@$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) restart $(c)

status: ## Show status of containers
	@$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) ps

ps: status ## Alias of status

build: ## (re)Build all images or c=<name> containers
	@$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) build $(c)

manage/%: ## Execute manage commands
	@$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) exec web python manage.py $*

makemigrations: ## Execute makemigrations
	@$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) exec web python manage.py makemigrations

migrate: ## Execute migrate
	@$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) exec web python manage.py migrate

bash:
	@$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) exec $(c) bash

collectstatic:
	@$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) run web python manage.py collectstatic

logs:
	@$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) logs -f --tail=200 $(c)

pdb: ## Enable service ports to be able to use the debug
	@$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) run --service-ports $(c)


pdbshell/%: ## Runs any command on the specified pdb container. Ex: cmd="/bin/bash
	docker exec -ti `docker ps -f name=mangapy_$*_run -q` $(cmd)
