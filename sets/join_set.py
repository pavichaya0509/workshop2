set1 = {"a", "b", "f"}
set2 = {"d", "e", "f"}
set3 = set.union(set2)
print(set3)

set1 = {"a", "b", "f"}
set2 = {"d", "e", "f"}
set1.update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)