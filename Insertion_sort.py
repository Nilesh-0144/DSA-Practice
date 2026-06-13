arr=[10,1,32,54,2,5,6,7,22]

for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1

    arr[j+1]=key

print(arr)