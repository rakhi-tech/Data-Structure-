
def count_odd_digits(n: int) -> int:
    
    if n == 0:
        return 0
    
    count = 0
    while n > 0:
        digit = n % 10   
        if digit % 2 == 1:   
            count += 1
        n //= 10
    return count

# Example runs
print(count_odd_digits(5))    
print(count_odd_digits(25))   
print(count_odd_digits(12345)) 
print(count_odd_digits(0))    