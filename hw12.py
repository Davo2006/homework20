x = [1,2,3,4,5,6]
def function(list,n):
    if n == 0:
        return max(list)
    list.remove(max(list))
    return function(list,n-1)
print(function(x,4))