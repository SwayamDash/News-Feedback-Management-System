# Newsfeed-Management-System
The objective is to design and develop small working prototype of centralized newsfeed system.

## Description
A simple newsfeed management system which takes a text file containing the url of news sites.
Then extracts the individual news or stories from the news article and store these feeds as JSON files by date.
The JSON file contain fields such as current_date, story_date, story_time, body, title, source etc..

Some fields are described here:<br /> 
current_date - process date<br /> 
author - article author<br /> 
story_date - extract story date from article<br /> 
story_time - extract story time from article <br /> 
body - story text (cleaned text)<br /> 
title - story title<br /> 

## Features
1. No duplicity of feed.
2. Newsfeed document is stored in MongoDB database.
3. Articles captured on a specific date can be retrieved.

## Contents
* `news_scrapper,py` - to scrape the details from a given list of articles or news-websites
* `Scrapped_NewsFeed` - gives all the scraped details in json format


## Running locally
* Fork and clone the repo.
* `cd` to the API directory eg. cd Flask_Server_API
* Create an environment: <br />
   &nbsp;&nbsp;  - For macOS or Linux: `python3 -m venv environment` <br />
   &nbsp;&nbsp;  - For windows: `py -m venv environment`
* Activate the Flask-python environment by: <br /> 
   &nbsp;&nbsp;  - For macOS or Linux:  `source environment/bin/activate`
   &nbsp;&nbsp;  - For windows: `environment\Scripts\activate`
* In the same environment, install all the packages specified in the Requirements.txt file.
* Run `python main.py` to start the server
* Open the browser and go to `http://localhost:8080/?date=dd/mm/yyyy`
* Give the date as an input given in the specified format, to retrieve all the news stories for the same day in JSON format.
