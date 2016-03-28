##Q6
faculty['first_name'] = faculty.name.str.split('\s+').str[0]
faculty['last_name'] = faculty.name.str.split('\s+').str[-1]
subset = faculty[["first_name","last_name", " degree", " title", ' email']]
tuples = [tuple(x) for x in subset.values]

dict = []

for i in range(0,len(tuples)):
    d = {
        tuples[i][1:2]: [tuples[i][2:5]]
    }
    dict.append(d)

dict[0:3]


##Q7

dict1 = []

for i in range(0,len(tuples)):
    d = {
        (tuples[i][0:2]): [tuples[i][2:5]]
    }
    dict1.append(d)

dict1[0:3]

##Q8

dict2 = []

for i in range(0,len(tuples)):
    d = {
        (tuples[i][1:2] + tuples[i][0:1]): [tuples[i][2:5]]
    }
    dict2.append(d)

dict2[0:3]
