thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict["color"] = "red"
print(thisdict) #output{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.update({"color": "red"})
print(thisdict) #output{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}