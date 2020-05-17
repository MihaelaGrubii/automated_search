#!/usr/bin/env python3
#
import sys
from filegenerator import addToFile
from filegenerator import addToDocx
from googlesearch import search

'''Input Reader - main class

This script reads the arguments inputed by user, and using google search lib fires up a search for n number of searched
sources, if the user gives 0 additional arguments user is prompted with an Error Message, if the user does forget to specify
noumber of sources needed he will be given 5 by default; This script will generate 2 files *ToFile will generate a DocX and
*ToDocx will generete a doc file.
'''
print('Argument List:', str(sys.argv))

searched_topic = list(sys.argv)
del searched_topic[0]
try:
    nbr_searches = int(searched_topic[-1])
except ValueError:
    nbr_searches = 5
    searched_topic.append(str(nbr_searches))
del searched_topic[-1]
topics = []

if len(searched_topic) == 0:
    print("Try again, and try to give some arguments to fire up the search.")
else:
    query = ' '.join(searched_topic)
    for i in search(query, tld='com', lang='en', tbs='0', safe='off', num=nbr_searches, start=0, stop=nbr_searches, domains=None, pause=2.0, tpe='', country='', extra_params=None, user_agent=None):
        topics.append(i)
    addToDocx(query, topics, nbr_searches)
    addToFile(query, topics, nbr_searches)
