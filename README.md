# AutomationPratice in Python

This repository was created to study automation with Python and Selenium

## Requirements

Python 3

Some updated browser (Chrome, Firefox, etc)

The correspondent driver of your browser (change the driver path in conftest if you need)
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```

## Usage
To run all tests, go to the root folder of the project and execute the command
```bash
pytest --browser chrome
```

To run some specific test, go to the root folder of the project and execute the command
```bash
pytest --browser chrome tests/path_to_test.py
```
