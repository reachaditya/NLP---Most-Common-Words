# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 23:06:57 2018

@author: adity
"""

#Import the Liabraries
from bs4 import BeautifulSoup
import urllib.request
import nltk

# Fetching the data from the URL
response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")

# Import some Liabraries for word count
from collections import Counter
from string import punctuation

# Get the words within paragrphs
text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
c_p = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))

# Get the words within divs
text_div = (''.join(s.findAll(text=True))for s in soup.findAll('div'))
c_div = Counter((x.rstrip(punctuation).lower() for y in text_div for x in y.split()))

# Sum the two countesr and get a list with words count from most to less common
total = c_div + c_p
list_most_common_words = total.most_common() 
total.most_common() # Prints most common words staring at most common.