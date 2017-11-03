#!/usr/bin/env python3

"""Merge all PDF Files in a folder into one. 

	Usage: <officeclerk.py> <path>

	Default path is '.'

	@Niklas Kleemann, 2017
"""

import PyPDF2
import os
import sys


if len(sys.argv) < 2:
	path = '.'
else:
	path = sys.argv[1]

files = []

for file in os.listdir(path):
	if file.endswith('.pdf'):
		files.append(file)
	files.sort(key = str.lower)

pdf_writer = PyPDF2.PdfFileWriter()

for file in files:
	file_obj = open(file, 'rb')
	pdf_reader = PyPDF2.PdfFileReader(file_obj)

	for page_n in range(0, pdf_reader.numPages):
		page_obj = pdf_reader.getPage(page_n)
		pdf_writer.addPage(page_obj)

out = open('out.pdf', 'wb')
pdf_writer.write(out)
out.close()


