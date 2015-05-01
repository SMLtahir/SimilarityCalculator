-include .env
export PYTHON=$(PYTHONPATH)/python

all: load_neighbors

load_neighbors:
	$(PYTHON) load_neighbors.py

test:
	$(PYTHON) $(SIMCALC_HOME)/test/unit_tests_load_neighbors.py

.PHONY: clean load_neighbors test

clean:
	rm -rf data/*
