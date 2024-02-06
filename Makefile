SHELL := /bin/bash
.PHONY: virtual run clean check
VENV := venv-graph
PYTHON := $(VENV)/bin/python3
PYTEST := $(VENV)/bin/pytest
MYPY := $(VENV)/bin/mypy
PIP := $(VENV)/bin/pip
SRC-FILES := $(wildcard src/graphs/*.py)
TEST-FILES := $(wildcard tests/*.py)

all: virtual run

$(VENV)/bin/activate: requirements.txt
	@echo "Creating virtual environment"
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt 2>&1|tee -a build.log

# shortcut target
#virtual: $(VENV)/bin/activate:
#	echo "Activating virtual environment"
#./venv-ig/bin/activate

# Builds the distribution wheel
build: $(VENV)/bin/activate $(SRC-FILES)
	$(PYTHON) -m build

# Performs static type checking for all source files using mypy
lint: $(VENV)/bin/activate
	@echo "Type checking files..." $(SRC-FILES)
	$(MYPY) --ignore-missing-imports $(SRC-FILES)
	$(MYPY) --ignore-missing-imports $(TEST-FILES)

# Run the main application
run: $(SRC-FILES)
	@echo "Running main application"
	$(PYTHON) src/graphs/main.py
	
# Runs unit tests with pytest
test: $(SRC-FILES) $(TEST-FILES)
	$(PYTEST)

# Cleans the byte code cache and virtual environment
clean:
	@echo "Cleaning the house.."
	rm -rf **/*egg-info
	rm -rf dist/*
	rm -rf **/__pycache__
	rm -rf $(VENV)
