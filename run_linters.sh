#!/bin/bash

flake8 ./preconditions ./tests ./conftest.py ./tools ./http_service
echo "linters done"
