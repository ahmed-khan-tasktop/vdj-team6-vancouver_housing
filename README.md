# Vancouver Housing
- Team
- Overview
- Repo content
- Setup
- Web App deployment
	- local 
	- host
- Acknowledgment

## Team
Team lead: ahmed khan

Mentor: Alice Ai

Documentation: All

Scripting: Faisal, Dillon, Mask,

Modelling: All

Sanity checking: All

## Overview
This project is part of the Vancouver Datajam 2021. In this project we are examing 2 datasets; a non-market-housing
dataset and property tax between the years 1958 - 2020.

The [non-market-housing](https://opendata.vancouver.ca/explore/dataset/non-market-housing/information/) and [property tax](https://opendata.vancouver.ca/explore/dataset/property-tax-report/information/) are provided by the city of vancouver open data initiative. The data is provided under the [Open Government Licence](https://opendata.vancouver.ca/pages/licence/).

## Repo Content

- app: Flask app with static files to build a web app.
- data:
	- non-market-housing.csv: As mentioned in the overview, this dataset is for the development projects
		between 1958-2020.

- notebooks: This folder contains jupyter and tableau notebooks with data exploration for both datasets, wrangling and visualization. For more information about the notebooks check the README.md in the notebooks folder.
- app.py: a flask app with interactive map and graphs of the non market housing dataset.
- etl_data.py: helper python module for data wrangling used in app.py file for visualization.
- Procfile: Used for Heroku deployment. A set of instructions for Heroku to run certain commands/processes.

## Setup
- Tableau:
This is a straight forward setup. Download tableau and follow the setup prompts. This allows to explore the different
tableau files in the notebooks folder.
- Python/Jupyter:
	- Create a virtual environment from the project root dir using `$python3 -m venv env`
	- Activate the vritual environment `$source env/bin/activate`
	- Install the required libraries  `$pip install -r requirements.txt`
	- Install jupyter `$pip install -r jupyter`. To run a jupyter notebook `$jupyter <filename.ipynb>`, this will open
		jupyter in the browser.



## Web app
Before starting, make sure you have the virtual environment activated and that the `requirements.txt` is installed. (see setup).
To run the app:
	- Activate virtual environment.
	- Run `$export MAPBOX_TOKEN=<mapbox_api_token>`. This creates an Env variable which is used in the app to make api calls to mapbox. A token can be obtain from mapbox following this [link](https://help.mapsly.com/en/articles/5344496-how-to-sign-up-for-a-mapbox-account-and-create-an-access-token)
	- Run `$python app.py`. This starts a flask server by default at http://127.0.0.1:8050/. You can open this url in the browser to make sure the app is running.

Deploy a git repo to Heroku :
	- Fork the repo from git.
	- Follow the instructions to [deploy to Heroku](https://devcenter.heroku.com/articles/git).
	- In Heroku, go to your account -> dashboard -> click on the pushed app name -> settings.
	Under settings, Config Vars section click on 'Reveal Confg Vars'. Set key to `MAPBOX_TOKEN` and value to
	mapbox api token.

## Acknolwedgement
Thanks to [Vancouver Datajam](https://www.vancouverdatajam.ca) for arranging for this years 100% online event. It takes innovationa and alot of effort to make this event happen.
Thanks for the City of Vancouver and its initiateve to maintain openness and provide the datasets freely.
