Pandemic Forecasting Assessment
===============================

[GitHub](https://github.com/Nasiemjr/pandemic-forecasting/tree/master)

This Assessment can be divided into 4 parts (folders):
---------------------------------------------------
- API
- Improve Accuracy
- Jupyter Notebook
- Web Application

API
---
- This folder contains a python Flask API.
- This API will scrape the data from the website and use the ARIMA model to forecast new cases for the next 7 days.
- The following packages will need to be installed using "pip install":
   - sklearn
   - statsmodels
   - flask
   - datetime
   - flask_cors
   - pandas
   - bs4
   - requests
   - json
   - re
- Once the packages have been installed, follow the below steps to run the API:
  - Navigate to the folder contaning the API.
  - Open up a terminal in that folder.
  - Execute the line "python main.py".
  - It will show that it is running on "http://127.0.0.1:5000".

Improve Accuracy
----------------
- This folder contains a text file named "Improve_Forecast_Accuracy.txt".
- This text file contains a short paragraph on how the forecasting of the pandemic cases can be improved using additional data.

Jupyter Notebook
----------------
- This folder contains the following files:
  - pandemic_forecasting.ipynb: A Jupyter Notebook that contains step by step sections on how the data was scraped from https://www.worldometers.info/coronavirus/country/south-africa/ and prepared for the ARIMA model.
  - data.csv: A CSV containing the next 7 days dates with the respective new cases for that day.
  - new_cases_by_date.png: A line diagram of the new cases by date.

Web Application
----------------
- This folder contains a simple React web application that is used to call the Flash API and use that data to plot a line graph of the next 7 days forcasted cases.
- How to install the packages:
   - Navigate to the folder "Web Application".
   - Open up a terminal in this folder.
   - Execute the line "npm install" to install all the required packages.
- How to run the application:
   - Once that has completed, execute the line "npm start".
   - It will run on "http://localhost:3000/".
   - NOTE: Ensure that the Flask API is running before running the web application.
     
