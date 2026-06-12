def bubble_Sort(arr):
    for i in range(len(arr)):
        bubble=0
        
        for j in range(1,len(arr)-i):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
                bubble=1

        if bubble==0:
            break

    return(arr)

arr=[1,44,223,53,12,5]
print(bubble_Sort(arr))