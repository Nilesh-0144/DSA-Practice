# Problem: Second Largest Element

arr = [1, 2, 4, 7, 7, 5]

largest = float('-inf')
second = float('-inf')

for x in arr:
    if x > largest:
        second = largest
        largest = x
    elif x > second and x != largest:
        second = x

print("Second largest element is:",second)
