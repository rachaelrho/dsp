##Q1
stringDegree = str(faculty[' degree'])
degrees = set(faculty[' degree'])
frequency = []

for degree in degrees:
    a = re.findall(degree, stringDegree)
    frequency.append(degree)
    frequency.append(len(a))

##Q2
stringTitle = str(faculty[' title'])
titles = set(faculty[' title'])
frequency = []

for title in titles:
    a = re.findall(title, stringTitle)
    frequency.append(title)
    frequency.append(len(a))

##Q3

import re

hand = open('C:\\Users\\rrho002\\Desktop\\Personal\\Metis\\faculty.txt')

for line in hand: 
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        print x

##Q4

import re

hand = open('C:\\Users\\rrho002\\Desktop\\Personal\\Metis\\faculty.txt')
email = []

for line in hand: 
    line = line.rstrip()
    x = re.findall('@(.*)$', line)
    if len(x) > 0:
        email.append(x)

print(np.unique(np.array(email)))
