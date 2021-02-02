hi:
	echo hi


pypi:
	rm -rf __pycache__
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
	rm -rf build dist *.egg-info