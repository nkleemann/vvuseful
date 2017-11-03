#!/usr/bin/env python3

"""Download every image in a 4chan thread.

	Usage: chandl.py <thread_url> <folder_to_save>

   @Niklas Kleemann, 2017
"""

import requests
import bs4
import sys
import os

if len(sys.argv) < 3:
	print("Expected url and path..")
	sys.exit(1)

url  = sys.argv[1]
path = sys.argv[2] 

os.makedirs(path, exist_ok=True)
res = requests.get(url)
res.raise_for_status()

chan_soup = bs4.BeautifulSoup(res.text, 'html.parser')
chan_imgs = chan_soup.select('.fileText a')

if chan_imgs == []:
	print("[*] No images found.")
	sys.exit(1)
else:
	for img_src in chan_imgs:

		img_url = img_src.get('href')[2:]
		
		print("[*] Downloading image %s" % ('http://' + img_url))

		res = requests.get('http://' + img_url)
		res.raise_for_status()

		out = open(os.path.join(path, os.path.basename(img_url)), 'wb')

		for chunk in res.iter_content(100000):
			out.write(chunk)

		out.close()
