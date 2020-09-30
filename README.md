# Newsfeed-Management-System
The objective is to design and develop small working prototype of centralized newsfeed system.

## Description
A simple newsfeed management system which takes a text file containing the url of news sites.
Then extracts the individual news or stories from the news article and store these feeds as JSON files by date.
The JSON file contain fields such as current_date, story_date, story_time, body, title, source etc..

The fields are described here:<br /> 
 
author - article author<br /> 
current_date - process date<br />
story_date - extract story date from article<br /> 
story_time - extract story time from article <br /> 
body - story text (cleaned text)<br /> 
title - story title<br />
source - source of the news<br />

## Features
1. No duplicity of feed.
2. Newsfeed document is stored in MongoDB database.
3. Articles captured on a specific date can be retrieved.

## Contents
* `news_scrapper.py` - to scrape the details from a given list of articles or news-websites
* `Scrapped_NewsFeed.json` - gives all the scraped details in .json format
* `Flask_Server_API/Requirements.txt` - contains all the packages required to be installled, to run the program.
* `db.py` - connects the API to MongoDB cluster 
* `main.py` - Initiates a local host development server(Here: http://0.0.0.0:8080/)

## Running locally
* Fork and clone the repo.
* `cd` to the API directory eg. cd Flask_Server_API
* Create an environment: <br />
   &nbsp;&nbsp;  - For macOS or Linux: `python3 -m venv environment` <br />
   &nbsp;&nbsp;  - For windows: `py -m venv environment`
* Activate the Flask-python environment by: <br /> 
   &nbsp;&nbsp;  - For macOS or Linux:  `source environment/bin/activate` <br />
   &nbsp;&nbsp;  - For windows: `environment\Scripts\activate`
* In the same environment, install all the packages specified in the `Requirements.txt` file.
* Run `python main.py` to start the server
* Open the browser and go to `http://localhost:8080/?date=mm/dd/yyyy`. <br />
   &nbsp;&nbsp; Eg: `http://localhost:8080/?date=09/22/2020` outputs all the articles published on 09/22/2020.
* Give the date as an input given in the specified format(mm/dd/yyyy), to retrieve all the news stories published on the same day in JSON format.

## Thank you
