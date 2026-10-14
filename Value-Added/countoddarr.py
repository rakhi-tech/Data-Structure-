def count_odds(n, arr):
    count = 0
    for i in range(n):
        if arr[i] % 2 != 0:   # odd check
            count += 1
    return count

# Example runs
print(count_odds(5, [1, 2, 3, 4, 5]))   # Output: 3
print(count_odds(6, [1, 2, 1, 1, 5, 1])) # Output: 5
