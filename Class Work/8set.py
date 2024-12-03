a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = {5, 6, 7, 8, 9, 10, 11, 12, 13}

print("Set a:", a)
print("Set b:", b)

print("Length of set a:", len(a))
print("Type of set a:", type(a))
print("Length of set b:", len(b))
print("Type of set b:", type(b))

a.add(10)
print("Set a after adding 10:", a)

a.remove(8)
print("Set a after removing 8:", a)

print("Union of a and b:", a.union(b))
print("Intersection of a and b:", a.intersection(b))
print("Difference of a and b:", a.difference(b))
print("Symmetric difference of a and b:", a.symmetric_difference(b))
print("Is a subset of b:", a.issubset(b))

new_list = [2, 3, 4]
a.update(new_list)
print("Set a after joining with new list:", a)
