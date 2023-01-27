MODULE := level_calculator

setup:
	@poetry install

run:
	@python -m $(MODULE)

test:
	@pytest

lint:
	@echo "Running Flake8 against source and test files..."
	@flake8
	@echo "Running Bandit against source files...."
	@bandit -r --ini setup.cfg

clean: 
	rm -rf .pytest_cache

.PHONY: clean test