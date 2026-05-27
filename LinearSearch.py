def linear_Search(arr, K):

    for i in range(len(arr)):

        if arr[i] == K:
            return i

    return -1


arr = [1,3,2,4,5,4]
K = 4

print(linear_Search(arr, K))