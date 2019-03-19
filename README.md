# dash-template
A Dash template setup I use for component development

### Quick setup

*Clone* the repo:
```bash
$ git clone git@github.com:thinkjrs/dash-template
$ cd dash-template
```

*Install* dependencies w/`conda`:
```bash
$ conda-env create -f environment.yml
```

*Activate* your new `dash-template` virtual environment:
```bash
$ conda activate dash-template
```

*Run* your new barebones `Dash` application on port `8050`:
```python
python app/app.py
```

### Configuration

Tests and application code are separate and both need to be run from the
main project directory (i.e. the directory name you cloned this into).

##### `tests`
There are **two** `conftest.py` files: `conftest.py` and `tests/conftest.py`,
where the first is empty and the later a fixture-monkey patch.  
No configuration is necessary for the empty `conftest.py`.

In the second, `tests/conftest.py`, you need to change the `handle` param
to represent the difference between your `HOME` environment variable
and the path to this main project directory. Ultimately, `handle` needs
to point to the place from which you'd `run` (`python app/app.py`) the 
Dash application.

### Run your `tests`

Run the following `py.test` command from the main project directory
to run the any files starting with test\_ in the `tests` directory. This
runs all tests.

```bash
$ pytest -vv
```

Run a specific test, `test_my_specific_test_case.py`:
```bash
$ pytest tests/test_my_specific_test_case.py -vv
```
