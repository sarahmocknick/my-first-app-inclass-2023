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

ALPHAVANTAGE_API_KEY="_________"
```
SENDGRID_API_KEY="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"
SENDER_ADDRESS="sem319@georgetown.edu"

## Usage

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
python -m app.unemployment
```
Send an example email:
```sh
python app/email_service.py
```