def append(list1, list2):
    return list1 + list2

def concat(lists):
    result = []
    for item in lists:
        result = append(result, item)
    return result

def filter(function, lst):
    return [item for item in lst if function(item)]

def length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

def map(function, lst):
    return [function(item) for item in lst]

def foldl(function, lst, initial):
    acc = initial
    for el in lst:
        acc = function(acc, el)
    return acc

def foldr(function, lst, initial):
    acc = initial
    # To process from the right, we iterate over the reversed list
    for el in reverse(lst):
        acc = function(acc, el)
    return acc

def reverse(lst):
    result = []
    for item in lst:
        # Building the list backwards
        result = [item] + result
    return result
