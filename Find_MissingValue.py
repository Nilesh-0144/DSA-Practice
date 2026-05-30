arr=[1,2,4,5]
n=5
arr_sum=sum(arr)
exact_sum=0
for i in range(1,n+1):
    exact_sum+=i

print(exact_sum-arr_sum)

