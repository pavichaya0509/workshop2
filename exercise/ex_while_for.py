number = int(input("Enter number is : "))
print("while loop")
multiple = 0
while multiple < 12:
    multiple += 1
    print(number, "*", multiple, ":",number * multiple)
    if multiple > 12:
        break

print("-------------------------------------------------")
print("for loop")
for mul in range(multiple):
    mul += 1
    if mul <= 12:
        print(number,"*",mul,":",(number*mul))
    else:
        break