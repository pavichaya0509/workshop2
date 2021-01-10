x = "awesome"

def myFunc():
    global x # x = awesome
    print("Python is "+ x)
    x = "fantastic"

myFunc()
print("Python is "+ x)