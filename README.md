# Internet speed monitor

![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)

Python Script to automatically gather speedtest data from speedtest.net. Ping, Download Speed and Upload speed are fetched and stored in a csv file.

## Features:

* Automatic, just run the script
* Saves data in csv file for easy analysis

## TODO

- [ ] Implement a log file
- [ ] Add command line arguments I.E run for a specific time, or store results in megabytes/bits
- [x] Implement a config file
- [ ] General exception handling

## Installation

Install required packages:
`pip install -r requirements.txt`

Create a csv file with the headings `Date,Time,Ping,Download,Upload` or on the first run uncomment the `writer.writeheader()`

Run:
`python Main.py`

## Contact
samsimss98@gmail.com




