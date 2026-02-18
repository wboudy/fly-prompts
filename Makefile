.PHONY: build lint check

build:
	python3 scripts/build_palette.py

lint:
	python3 scripts/lint_palette.py

check: lint build
