# 2021 NYC Mayoral Webscraper

This project is designed to allow you to scrape the NYC Board of Elections (BOE) websites to obtain the details of all ranked-choice voting (RCV) rounds for each cadidate and export it to a CSV file.

## 2021_nyc_mayoral_webscraper.py

This is a Python script designed to allow you to input the relevant URL and number of rounds of ballots processed to obtain a CSV file of the results. For the URL, be sure to remove the round number suffix at the end of the address.

For the June 30 results, the following 	would be the relevant inputs:

```
Enter current URL with the terminal round number removed: https://web.enrboenyc.us/rcv/024306_

Enter number of rounds reported: 9
```

## 2021_nyc_mayoral_webscraper.ipynb

This is a Jupyter notebook version of the script above that will allow the code to be run in a web browser using Binder. 

To create a new CSV file using Binder, launch Binder by clicking on the button below. Then run the code block in the Jupyter notebook. A new CSV file will be avaiable in the working directory of the GitHub repository in Binder.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jessicaw9910/2021_nyc_mayor/HEAD)

## names.txt

This contains the names of the rows in the table on the BOE website. It is an input of the scripts and Jupyter notebook.

## output.csv

This is an example of the CSV file that will be output using the details from the June 30 round above.