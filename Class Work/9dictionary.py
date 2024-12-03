employee = {
    "name": "A",
    "age": 40,
    "type": {"developer": ["ios", "android"]},
    "permanent": True,
    "salary": 30000,
    100: (1, 2, 3),
    4.5: [5, 6, 7, 1]
}

print(len(employee), type(employee))

print(employee["type"]["developer"])

employee["permanent"] = False

employee["gender"] = "male"

del employee["age"]

print(employee.keys())
print(employee.values())
print(employee.items())

for key, value in employee.items():
    print(key, value)
