a = (1, 3, 5, 7, 4)

sum_odd = sum(x for x in a if x % 2 != 0)
print("Sum of all odd numbers:", sum_odd)

third_element = a[2]
print("Third index element:", third_element)

count_odd = sum(1 for x in a if x % 2 != 0)
count_even = sum(1 for x in a if x % 2 == 0)
print("Count of odd numbers:", count_odd)
print("Count of even numbers:", count_even)

a_extended = a + (2, 4, 6)
print("Extended tuple:", a_extended)

a_with_new_item = a[:2] + (400,) + a[2:]
print("Tuple after adding 400 at index 2:", a_with_new_item)

a_without_last = a[:-1]
print("Tuple after removing the last element:", a_without_last)

sliced_a = a[-4::-1]
print("Sliced tuple [-4::-1]:", sliced_a)

print("Tuple elements (skip 5):")
for x in a:
    if x == 5:
        continue
    print(x)
