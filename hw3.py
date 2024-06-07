def function(list):
    return sum([x for x in list if x%7==0])
print(function(range(100)))