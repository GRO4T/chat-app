#!/bin/bash
git_repo_root=$(git rev-parse --show-toplevel)
source $git_repo_root/.venv/bin/activate
PYTHONPATH=$PYTHONPATH:.. python3 -m unittest