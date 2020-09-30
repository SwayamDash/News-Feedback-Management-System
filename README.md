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
