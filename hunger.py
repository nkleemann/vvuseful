#!/usr/bin/env python3

"""Display the canteen menu (HTWK) w/o bullshit. 
   @Niklas Kleemann, 2017
"""

import requests
import bs4

raw  = requests.get('https://www.studentenwerk-leipzig.de/mensen-cafeterien/speiseplan?location=118')
food = bs4.BeautifulSoup(raw.text, 'html.parser').select(".meals__name")

for meal in food:
	print(meal.getText())