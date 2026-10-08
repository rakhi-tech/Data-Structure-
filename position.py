a="abcdefchfsdkidefg"
arr=[0]*26
for i in range(len(a)):
    arr[ord(a[i])-97]+=1
for i in range(len(arr)):
    print(chr(i+97)," -> ",arr[i])