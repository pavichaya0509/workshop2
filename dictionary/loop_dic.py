thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

for key in thisdict:
    print(key)
# output
# brand
# model
# year

for key in thisdict:
    print(thisdict[key])
# output
# Ford
# Mustang
# 1964

for key in thisdict.keys():
    print(key)
# ouput
# brand
# model
# year

for value in thisdict.values():
    print(value)
# output
# Ford
# Mustang
# 1964

for key, value in thisdict.items():
    print(key, value)
# output
# brand Ford
# model Mustang
# year 1964
