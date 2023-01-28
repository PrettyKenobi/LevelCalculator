setup:
	@poetry install

test:
	@pytest

clean: 
	rm -rf .pytest_cache

.PHONY: clean test