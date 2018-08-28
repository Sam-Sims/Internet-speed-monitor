# Internet-speed-monitor
![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)

Python program to automatically run a speedtest on speedtest.net, and store the results in an easy to read CSV file.

## Main Features

* Retrieves your current upload, download and ping from the offical speedtest.net servers.
* Stores the data in a csv file.
* Visulises the data, by plotting a graph of upload and download speed over time.


## Installing

Ensure Python 3.7 is installed and up to date.

Install dependencies.

```
pip install -r requirements.txt
```

Decide what webdriver you want to use, either chrome or firefox.

Firefox: https://github.com/mozilla/geckodriver/releases
Chrome: http://chromedriver.chromium.org/downloads

Fill in the config file to point the program to the installed webdriver.

## Usage

Run the speedtest first to create the CSV files of the data, stored in speeds.csv

`python Main.py`

Run the analyser to create the graph

`python Analyse.py`

A good idea is to use CRON or windows task scheduler to run the python script every x Minutes, to generate a lot of data to graph.

