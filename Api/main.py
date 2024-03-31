from sklearn.model_selection import train_test_split
from statsmodels.tsa.arima.model import ARIMA
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from flask_cors import CORS
import pandas as pd
from bs4 import BeautifulSoup
import requests
import json
import re

app = Flask(__name__)
CORS(app)

def scrap_data():
    url = 'https://www.worldometers.info/coronavirus/country/south-africa/'

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    all_scripts = soup.find_all('script')

    for number, script in enumerate(all_scripts):
        if 'graph-active-cases-total' in script.text:
            hcText = script.text

    # Get the x values using regular expression
    pattern = r"data:\s*\[(.*?)\]"
    match_x = re.search(pattern, hcText, re.DOTALL)

    if match_x:
        data_str_x = match_x.group(1)
        data_list_x = json.loads("[" + data_str_x + "]")
    else:
        print("Data array not found.")

    # Get the y values using regular expression
    pattern = r"categories:\s*\[(.*?)\]"
    match_y = re.search(pattern, hcText, re.DOTALL)

    if match_y:
        data_str_y = match_y.group(1)
        data_list_y = json.loads("[" + data_str_y + "]")
    else:
        print("Data array not found.")

    return data_list_x, data_list_y

def split_data():
    data_list_x, data_list_y = scrap_data()
    # Split the data into a train and test set
    train, test = train_test_split(data_list_x, test_size=0.34, random_state=42)
    history = [x for x in train]

    return history

def get_next_days(n):
    # Get today's date
    today = datetime.today()

    # List to store the next 7 days as strings
    next_seven_days = []

    # Loop through the next 7 days
    for i in range(1,n):
        # Calculate the date for the next day
        next_day = today + timedelta(days=i)
        # Format the date as a string in the 'Feb 15, 2020' format
        next_seven_days.append(next_day.strftime('%b %d, %Y'))

    # Print the list of next 7 days as strings
    return next_seven_days

def fit_model():
    history = split_data()
    model = ARIMA(history, order=(2, 1, 2))
    model_fit = model.fit()
    output = model_fit.forecast(7)
    next_7_days = get_next_days(8)
    return output.tolist(), next_7_days

@app.route("/")
def new_cases():
    output, next_7_days = fit_model()
    return jsonify(Forecasts=output,Next7Days=next_7_days)

if __name__ == '__main__':
    app.run(debug=True)