.DEFAULT_GOAL := test

FILES :=                 \
	application.py       \
    application_test.py  \
    app/candidate.py     \
    app/election.py      \
    app/party.py         \
    app/state.py 		 \
    .gitignore			 \
    makefile			 \
    apiary.apib			 \
    requirements.txt

ifeq ($(shell uname), Darwin)          # Apple
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(CI), true)                # Travis CI
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3
    AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Docker
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint3.5
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.4
    AUTOPEP8 := autopep8
endif

COVERAGE_FILES := application.py,candidate.py,election.py,party.py,state.py

.pylintrc:
	$(PYLINT) --disable=locally-disabled,no-member,too-few-public-methods --reports=no --generate-rcfile > $@

html: application.py
	$(PYDOC) -w application

log:
	git log > IDB1.log

format:
	$(AUTOPEP8) -i app/candidate.py
	$(AUTOPEP8) -i app/election.py
	$(AUTOPEP8) -i app/party.py
	$(AUTOPEP8) -i app/state.py

pylint: .pylintrc 
	-$(PYLINT) application_test.py
	-$(PYLINT) app/*.py

application_test.tmp: application.py application_test.py pylint
	$(COVERAGE) run    --branch --source=$(COVERAGE_FILES) application_test.py >  application_test.tmp 2>&1
	$(COVERAGE) report -m                      >> application_test.tmp
	cat application_test.tmp

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  .pylintrc
	rm -f  *.pyc
	rm -f  *.html
	rm -f  IDB1.log
	rm -f  application_test.tmp
	rm -rf __pycache__

test: html log application_test.tmp check

versions:
	which make
	make --version
	@echo
	which git
	git --version
	@echo
	which $(PYTHON)
	$(PYTHON) --version
	@echo
	which $(PIP)
	$(PIP) --version
	@echo
	which $(PYLINT)
	$(PYLINT) --version
	@echo
	which $(COVERAGE)
	$(COVERAGE) --version
	@echo
	which $(PYDOC)
	$(PYDOC) --version
	@echo
	which $(AUTOPEP8)
	$(AUTOPEP8) --version
	@echo
	$(PIP) list