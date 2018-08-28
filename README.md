# Internet speed monitor

![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)

Python Script to automatically gather speedtest data from speedtest.net. Ping, Download Speed and Upload speed are fetched and stored in a csv file.

## Features:

* Automatic
* Saves data in csv file for easy analysis via analysis.py
* Plots a graph of download and upload speeds over the time period

## TODO

- [x] Implement a config file
- [ ] Implement a log file
- [ ] Add command line arguments I.E run for a specific time, or store results in megabytes/bits

## Installation

Install required packages:
`pip install -r requirements.txt`

Create a csv file with the headings `Date,Time,Ping,Download,Upload` or on the first run uncomment the `writer.writeheader()`

Run:
`python Main.py`

Analysis:
`python Analyse.py`



