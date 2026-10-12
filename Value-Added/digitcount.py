#count the number of digits in a given number
def count_digits(n: int) -> int:
    # Special case: if n is 0, return 1
    if n == 0:
        return 1
    
    count = 0
    while n > 0:
        count += 1
        n //= 10   # remove last digit
    return count

# Example runs
print(count_digits(4))   
print(count_digits(14))  
print(count_digits(0))   
print(count_digits(12345)) 