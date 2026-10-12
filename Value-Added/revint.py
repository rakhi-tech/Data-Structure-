
def reverseInteger(n: int) -> int:
    rev = 0
    while n > 0:
        digit = n % 10        # last digit
        rev = rev * 10 + digit  # build reversed number
        n //= 10              # remove last digit
    return rev

# Example runs
print(reverseInteger(25))    # Output: 52
print(reverseInteger(123))   # Output: 321
print(reverseInteger(100))   # Output: 1 (leading zeros removed)
print(reverseInteger(0))     # Output: 0
