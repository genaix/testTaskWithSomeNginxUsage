#!/bin/bash

flake8 --max-line-length=120 ./preconditions ./tests ./conftest.py ./tools ./steps ./http_service
echo "linters done"
