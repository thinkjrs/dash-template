"""
pytest configuration template

import your custom module and monkeypatch the PYTHONPATH
for a test run

****************
changes required 
****************
- We account for the HOME environment variable, change as needed

- Change <handle> below to reflect the path *after* your HOME to the 
    main project repository. 
    
    While in this directory an ls command would print
    something like app/ tests/ environment.yml README.md conftest.py. 
"""
import pytest
import os
import app

@pytest.fixture(autouse=True) # run automatically prior to tests
def pythonpath(monkeypatch):
    handle = '/dir/to/rootdir/'
    try:
        project_path = os.environ['HOME'] + handle
        monkeypatch.setenv('PYTHONPATH', project_path) 
    except KeyError as err:
        print(f"$HOME not present -> {err}")


