install:
	uv sync

gendiff:
	uv run gendiff

build:
	uv build

publish:
	uv publish --dry-run

package-install:
	uv tool install --force .

lint:
	uv run ruff check gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml