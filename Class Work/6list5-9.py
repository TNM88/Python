
a = [1, 3, 5, 7, 9]
new_list = [2, 4, 6]
a.extend(new_list)  
print("After joining:", a)

b = a.copy()
print("Copied list b:", b)

b.sort()
print("Sorted list b:", b)

print("Elements in b until 5:")
for element in b:
    if element == 5:
        print(element)
        break
    print(element)
    
largest_number = max(a)
print("Largest number in 'a':", largest_number)
