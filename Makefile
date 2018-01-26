init:
    pip install -r requirements

test:
    nosetests tests

.PHONY: init test