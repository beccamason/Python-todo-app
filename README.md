# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

Following the link to the Trello API, other .env variables are required.  These are: 
TRELLO_KEY - the key for your account submitted in all API calls 
TRELLO_TOKEN - the token for your key, also submitted in all API calls 
TRELLO_ID - the Board ID for the board you are wanting to interact with 

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Testing 

This app uses `Pytest`. The current unit tests are as follows: 
- Testing Pytest is working 
- Checking that 'Not Started' cards show in the view model 
- Same for 'Done' items 
- Same for 'In Progress' items 

There is also an integration test in place using mocking to simulate getting cards from the Trello API.

To action these tests run the following in the terminal: 
```bash 
$ poetry run pytest 
```

These tests can also be accessed from the testing pane within VS Code. 

##Docker 

This app uses 'Docker' to enable it to run through a container. 

To build only the development container run the following command: 
```bash 
docker build --target development --tag todo-app:dev .
```

To run the development container use: 
```bash 
docker run --env-file ./.env -p 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/todo_app/todo_app todo-app:dev
```

To build the production container run the following command: 
```bash 
docker build --target production --tag todo-app:prod .
```
 
To run the production container use: 
```bash
docker run --env-file ./.env -p 80:80 todo-app:prod .
```