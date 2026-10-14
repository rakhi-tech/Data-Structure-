def reverse_array(arr):
    n = len(arr)
    left, right = 0, n - 1
    while left < right:
        
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


print(reverse_array([1, 2, 3, 4, 5]))   # Output: [5, 4, 3, 2, 1]
print(reverse_array([1, 2, 1, 1, 5, 1])) # Output: [1, 5, 1, 1, 2, 1]
