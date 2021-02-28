# NRChallenge_Services

## Objective: ##
This project has the API which pushed emissions and other power plant-related data to the controller app. 
It is built using the Django framework and uses the default sqlite database as its data store

## How to set up on local: ##
- Clone the repo : ``` git clone https://github.com/sania-dsouza/NRChallenge_Services.git ```
- cd into the 'services' folder: ``` cd services ```
- Install dependencies: ``` pip install ```
-  Run the project by sending information to New Relic at the same time 
```
  NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program python manage.py runserver 4001
```

- View the project running at  http://127.0.0.1:4001/
- Start the 'power plant' by navigating to '/start' :  http://127.0.0.1:4001/start
This starts the service which emits a random emission value for CO2 , NOX and SO2 per minute 
- See the data emitted by navigating to /admin :  http://127.0.0.1:4001/admin

