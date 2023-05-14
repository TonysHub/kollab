# Setup
## Python Version
This project uses python 3.11.3. Whether you use local or virtual python version, please make sure you're using 3.11.3 to avoid any conflicts.

## Setup venv
At your BASE_DIR
```
$ python3 -m venv venv
$ source venv/bin/activate
$ poetry install
```

Now our setup is good to go :)


## Local settings
At your BASE_DIR create a folder `local`
```
$ mkdir local
```
Create `settings.dev.py` in `local` folder which will store your personal KEYS.
This file is in .gitignore.

Example,
```
SECRET_KEY = "YOUR_KEY"
POSTGRES_USERNAME = ""
POSTGRES_PW = ""
```
