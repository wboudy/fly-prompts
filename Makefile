.PHONY: build lint validate check

build:
	python3 scripts/build_palette.py

lint:
	python3 scripts/lint_palette.py

validate:
	python3 scripts/validate_palette_alignment.py

check: lint build validate
