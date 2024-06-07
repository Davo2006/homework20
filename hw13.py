a = {1,2,3}
b = {4,5,6}
def function(x:set,y:set):
    return x.isdisjoint(y)
print(function(a,b))