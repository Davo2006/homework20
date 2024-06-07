def function(list1,list2):
    x = []
    for e in list1:
        if e in list2 and e not in x:
            x.append(e)
    return x
print(function([12,3,4,1],[12,4,21,3]))