
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


print(factorial(2))   
print(factorial(0))   
print(factorial(5))   
print(factorial(7))   
