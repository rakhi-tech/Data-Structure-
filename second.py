arr = [10,3,4,56,78,46,78]
max = min = arr[0]
smin=smax=arr[0]
for num in arr:
    if num>max:
        max=num
    elif( num>smax and num!=max):
        smax = num
        if num<min:
            smin = min 
            min=num
        elif(num<smin and num!=min):
             smax=num
print("largest number is:",max)
print("secondlargest number is:",smax)  
print("smallest number is:",min) 
print("second smallest number is:",smin)         
                  



