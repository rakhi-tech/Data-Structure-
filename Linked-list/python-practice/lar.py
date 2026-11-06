n = int(input("Enter a number: "))
largest = 0

while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n //= 10

print("Largest digit =", largest)