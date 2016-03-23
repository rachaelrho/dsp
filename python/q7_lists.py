# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    length = filter(lambda x: len(x)>1 and x[:1] == x[-1:], words)
    print(len(length))


def front_x(words):
    sort = sorted(words, key =lambda x: (not x.startswith("x"), x))
    print(sort)


def sort_last(tuples):
    sort = sorted(tuples, key= lambda x: x[1])
    print(sort)


def remove_adjacent(nums):
    if len(nums) > 0:
        return [a for a, b in zip(nums, nums[1:]+[not nums[-1]]) if a != b]
    else:
        print([])


def linear_merge(list1, list2):
    newList = sorted(list1 + list2)
    print(newList)
