install:
	poetry install

lint:
	poetry run flake8 brain_games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

brain-games:
	poetry run brain-games

doall:
	poetry build && poetry publish --dry-run -n && python3 -m pip install --user --force-reinstall dist/*.whl

