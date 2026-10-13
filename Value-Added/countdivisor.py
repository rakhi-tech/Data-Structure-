def find_divisors(n):
    divisors = []
    for i in range(1, n+1):   # 1 ते n पर्यंत loop
        if n % i == 0:        # जर remainder 0 असेल तर i divisor आहे
            divisors.append(i)
    return divisors
