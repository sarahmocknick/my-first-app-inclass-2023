# my-first-app-inclass-2023
## Setup

Create and activate a virtual environment:

```sh
conda create -n my-first-env python=3.10

conda activate my-first-env
```
Obtain an [API Key from Alphavantage](https://www.alphavantage.co/support/#api-key) or from the prof (`ALPHAVANTAGE_API_KEY`).

Create a ".env" file and paste in the following contents:

```sh
# this is the ".env" file...
You must first follow the [setup instructions](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md) to create an account, verify your account, setup a single sender, and obtain an API Key.

ALPHAVANTAGE_API_KEY="_______"
```
SENDGRID_API_KEY="TODO"
SENDER_ADDRESS="example.gmail.com"

## Usage

### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

Run the example script:

```sh
python app/my_script.py
```

Install packages:
```sh
pip install -r requirements.txt
```

Run the unemployment report:
```sh
#python app/unemployment.py
#when importing we need to change usage command to this: (update your readme accordingly):
#python -m app.unemployment

```
Run the stocks report
```sh
python -m app.stocks


```
Send an example email:
```sh

python app/email_service.py
```

## Testing

Run tests:

```sh
pytest
```