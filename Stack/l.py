n = int(input("Enter number of elements: "))

lst = []
for i in range(n):
    lst.append(int(input()))

unique = []

for x in lst:
    if x not in unique:
        unique.append(x)

print("Unique elements:", unique)
