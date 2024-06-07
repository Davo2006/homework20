def check(string:str):
    if len(string.split("@"))==2 and string.split("@")[1].count(".") == 1 and string.split("@")[1].split(".") and len(string.split(".")) == 2:
        return True
    return False
print(check("example@gmail.com"))