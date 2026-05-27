arr=[0,1,3,0,2,0,0,1,00]

j=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[j],arr[i]=arr[i],arr[j]
        j+=1

print(arr)
