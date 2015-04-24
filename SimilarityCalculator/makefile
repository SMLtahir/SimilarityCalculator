include .env

PYTHON = $(ANACONDA_BINDIR)/python

all: load_neighbors

load_neighbors:
	$(PYTHON) load_neighbors.py

.PHONY: clean load_neighbors

clean:
	rm -rf data/*

