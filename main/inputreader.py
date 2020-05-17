#!/usr/bin/env python3
#
import sys
from filegenerator import addToFile
from filegenerator import addToDocx
from googlesearch import search

print('Argument List:', str(sys.argv))

searched_topic = list(sys.argv)
del searched_topic[0]
nbr_searches = int(searched_topic[-1])
del searched_topic[-1]
topics = []

if len(searched_topic) == 0:
    print("Try again, and try to give some arguments to fire up the search.")
else:
    query = ' '.join(searched_topic)
    print(query)
    for i in search(query, tld='com', lang='en', tbs='0', safe='off', num=nbr_searches, start=0, stop=nbr_searches, domains=None, pause=2.0, tpe='', country='', extra_params=None, user_agent=None):
        print(i)
        topics.append(i)
    addToDocx(query, topics, nbr_searches)
