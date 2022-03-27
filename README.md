# Stack Overflow and Indeed Scraper - Scraping job informations

Automatically scrapping the job information, and put the all the result in one excel file.


## [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Python library for scrapping

Beautiful Soup is a Python library for pulling data out of HTML and XML files. 
It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. 
It commonly saves programmers hours or days of work.

This document covers Beautiful Soup version 4.10.0. The examples in this documentation were written for Python 3.8.


## Run the code

You can download this file and run it. But this way is discouraged.

Recommend visit [Dawoon Kim replit](https://replit.com/@DawoonKim/WebScrapper#main.py), which does work very well for me.


## What does JobScrapper?

JobScrapper parses python job results (that in Stack Overflow and Indeed) easily and in a fast way. It allows you to extract all found.
Links and their titles and descriptions programmatically which enables you to process scraped data further.

First of all you need to understand that GoogleScraper uses **two completely different scraping approaches**:
+ Scraping with low level http libraries such as `requests` modules. This simulates the http packets sent by browsers.

JobScrapper is implemented with the following techniques/library:
+ Python 3.7
+ Beautiful Soup
