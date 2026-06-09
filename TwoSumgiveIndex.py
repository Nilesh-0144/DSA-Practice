arr = [2, 7, 4, 5, 3, 4]
target = 9
new = {}

for i in range(len(arr)):
    com = target - arr[i]

    if com in new:
        print([new[com], i])
        break

    new[arr[i]] = i