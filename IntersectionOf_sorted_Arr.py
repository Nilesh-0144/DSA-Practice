arr1=[1,2,3,3,4,2]
arr2=[2,3,5,6,7,8]
result=[]
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i]==arr2[j] and (arr1[i] not in result):
            result.append(arr1[i])

print(result)

