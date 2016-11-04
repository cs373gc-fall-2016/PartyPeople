.DEFAULT_GOAL := test

ifeq ($(shell uname), Darwin)          # Apple
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage
    PYDOC    := pydoc
    AUTOPEP8 := autopep8
else ifeq ($(CI), true)                # Travis CI
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint3.5
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint3.5
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.4
    AUTOPEP8 := autopep8
endif

COVERAGE_FILES := application.py

.pylintrc:
	$(PYLINT) --disable=locally-disabled,no-member,too-few-public-methods --reports=no --generate-rcfile > $@

html:
	find . -type f \( -name "*.py" \) | xargs $(PYDOC) -w

log:
	git log > IDB1.log

format:
	find . -type f \( -name "*.py" \) | xargs $(AUTOPEP8) -i

pylint: .pylintrc 
	find . -type f \( -name "*.py" \) | xargs $(PYLINT)

application_test.tmp: application.py application_test.py
	$(COVERAGE) run    --branch --source=$(COVERAGE_FILES) application_test.py >  application_test.tmp 2>&1
	$(COVERAGE) report -m                      >> application_test.tmp
	cat application_test.tmp

clean:
	rm -f  .coverage
	rm -f  .pylintrc
	rm -f  *.pyc
	rm -f  IDB1.log
	rm -f  application_test.tmp
	rm -rf __pycache__
	rm -rf ./*/*.pyc

test: html log applicaion_test.tmp check
