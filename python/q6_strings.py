# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    def donuts(count):
    if count < 10:
        print("Number of donuts: " + str(count))
    else:
        print("Number of donuts: many")


def both_ends(s):
    def both_ends(s):
    if len(s) > 2:
        print(s[:2] + s[-2:])
    else:
        print("")


def fix_start(s):
    first = str(s[:1])
    last = str(s[1:])
    new = string.replace(last,first,'*')
    print(first + new)


def mix_up(a, b):
    a1 = b[:2] + a[2:]
    b1 = a[:2] + b[2:]
    print(a1 + str(' ') + b1)
    


def verbing(s):
    if len(s) > 2:
        test = s[-3:]
        if test == 'ing':
            print(s + 'ly')
        else:
            print(s + 'ing')
    else:
        print(s)
    


def not_bad(s):
    substring1 = "not"
    substring2 = "bad"
    if substring1 in s and substring2 in s:
        substring1_pos = s.index(substring1) 
        substring2_pos = s.index(substring2) 
        if substring1_pos < substring2_pos:
            s = string.replace(s,s[substring1_pos:(substring2_pos+3)],'good')
            print(s)
        else:
            print(s)


def front_back(a, b):
    alen, blen = (len(a)+1)/2, (len(b)+1)/2
    return a[:alen] + b[:blen] +  a[alen:] + b[blen:]
    raise NotImplementedError
