all: install format lint test

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black . --line-length 100 --verbose

lint:
	ruff check src/ --fix --verbose

test:
	python -m pytest -vv src/
	python -m pytest -vv --nbval *.ipynb || true
	rm -rf *.png *.pdf

run:
	python src/main.py

deploy:
	git config --local user.email "41898282+github-actions[bot]@users.noreply.github.com"
	git config --local user.name "github-actions[bot]"
	git add NBA_2021_Report.pdf
	git add ./*.png
	git commit -m "Add report and images"