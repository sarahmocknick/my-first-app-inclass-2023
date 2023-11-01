#from getpass import getpass

#API_KEY = getpass("Please input your AlphaVantage API Key: ")
#Imports at the top
#modules
import os
import json
from pprint import pprint
from statistics import mean
#Packages
from dotenv import load_dotenv
import requests
from plotly.express import line

#Environment variables and constants
load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
print(API_KEY)

#Any functions

#breakpoint()
#pauses the execution of the program wherever you use it, allows us to interactively debug
#quit()
#stops - doesn't get to anything below but thinks that it is done, it doesn't continue to run or see anything below
#can also use python -i to make terminal interactive

#Working code

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)
print(type(parsed_response))
print(parsed_response.keys())
#pprint(parsed_response)

data = parsed_response["data"]

# Challenge A
#
# What is the most recent unemployment rate? And the corresponding date?
# Display the unemployment rate using a percent sign.

print("-------------------------")
print("LATEST UNEMPLOYMENT RATE:")
#print(data[0])
print(f"{data[0]['value']}%", "as of", data[0]["date"])


# Challenge B
#
# What is the average unemployment rate for all months during this calendar year?
# ... How many months does this cover?



this_year = [d for d in data if "2023-" in d["date"]]

rates_this_year = [float(d["value"]) for d in this_year]
#print(rates_this_year)

print("-------------------------")
print("AVG UNEMPLOYMENT THIS YEAR:", f"{round(mean(rates_this_year), 2)}%")
print("NO MONTHS:", len(this_year))

# Challenge C
#
# Plot a line chart of unemployment rates over time.


dates = [d["date"] for d in data]
rates = [float(d["value"]) for d in data]

fig = line(x=dates, y=rates, title="United States Unemployment Rate over time", labels= {"x": "Month", "y": "Unemployment Rate"})
fig.show()