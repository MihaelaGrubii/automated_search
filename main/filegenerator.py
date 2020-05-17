
import os.path
from os import path

counter = 0


def addToFile(name, content, nbr):
    topic = name
    name = (name.replace(' ', '')[:25])
    for char in name:
        if char in " ?.!/;:":
            name = name.replace(char, '')

    name = name + '.txt'
    counter += 1

    if path.exists(name):
        f = open(name, 'a+')
    else:
        f = open(name, 'w+')
        f.write('<<<This are the top ' + str(nbr) +
                ' results for your search!>>>\n')
        f.write('Topic: ' + topic.upper() + '\n')
    f.write('nbr.' + str(counter) + ' result: ' + content + '\n')
    f.close()
