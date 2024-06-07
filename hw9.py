x = {
    "a":5,
    "b":50,
    "c":25,
    "d":1
}
def function(dictionary:dict):
    max_value = 0
    max_key = None
    for key,value in dictionary.items():
        if value>max_value:
            max_value = value
            max_key = key
    return max_key
print(function(x))