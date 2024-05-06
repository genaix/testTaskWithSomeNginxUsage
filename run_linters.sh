#!/bin/bash

flake8 ./preconditions ./tests ./conftest.py ./tools
echo "linters done"
