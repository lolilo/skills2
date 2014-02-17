# Write a function that takes an iterable (something you can loop through, ie: string, list, or tuple) and produces a dictionary with all distinct elements as the keys, and the number of each element as the value
def count_unique(some_iterable):
    d = {}
    for i in range(len(some_iterable)):
        # if the element in some_iterable doesn't exist in d, instantiate the entry
        if not d.get(some_iterable[i]): 
            d[some_iterable[i]] = 1
        # if the element in some_iterable exists, add +1 to its amount 
        elif d.get(some_iterable[i]):
            d[some_iterable[i]] += 1
    return d

# Given two lists, (without using the keyword 'in' or the method 'index') return a list of all common items shared between both lists
# can still use loops and refer to things in list via indices -- but don't use the built-in function if x in list, etc. 
def common_items(list1, list2):
    common_items = []

    for i1 in list1:
        for i2 in list2:
            if i1 == i2:
                common_items.append(i1)
    return common_items

# Given two lists, (without using the keyword 'in' or the method 'index') return a list of all common items shared between both lists. This time, use a dictionary as part of your solution.
def common_items2(list1, list2):
    d = {}
    for i in range(len(list1)):
        # create a dictionary of all items in list1
        if not d.get(list1[i]):
            d[list1[i]] = 'exists'
        # if it already exists in the dictionary, pass
        elif d.get(list1[i]):
            pass

    common_items = []
    # check if items in list2 exist in dictionary        
    for i in range(len(list2)):
        if d.get(list2[i]):
            common_items.append(list2[i])

    return common_items



list1 = ['yo', 'yo', 'ha', 'no']
list2 = ['he', 'sells', 'no', 'sea', 'shells', 'yo']

print count_unique(list2)
print common_items2(list1, list2)
print common_items2(list1, list2)
