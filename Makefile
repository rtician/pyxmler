clean:
	find ./ -iname '*.pyc' -exec rm -f {} \;
	find ./ -iname '__pycache__' -exec rm -rf {} \;
	rm -rf dist/
	rm -rf *egg-info/
	rm -rf htmlcov/

test:
	pytest
