def sum(arr):
    freq={}
    for num in arr:
        freq[num] = freq.get(num,0)+1
    highest = max(freq.values())
    lowest=min(freq.values())
    return highest+lowest