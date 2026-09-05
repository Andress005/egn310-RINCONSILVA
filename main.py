items = [
    "Chevrolet",
    "Mazda",
    "Toyota",
    "Kia",
    "Hyundai",
    "Porche",
    "Ferrari",
    "Honda"
]
print("original order:")
print(items)

print("\nAlphabetical order:")
print(sorted(items))

print("\nReverse order:")
items.sort(reverse=True)
print(items)