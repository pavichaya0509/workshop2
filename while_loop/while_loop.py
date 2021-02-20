#1
i = 1
while i < 5:
    print(i)
    i += 1

i = 1

#2
while i < 5:
    print(i)
    i += 1

i = 1

#3
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 0

#4
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#5
i = 1

while i < 3:
    print(i)
    i += 1
else:
    print("i is no longer less than 3")