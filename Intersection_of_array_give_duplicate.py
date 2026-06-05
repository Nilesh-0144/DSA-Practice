def intersection(num1,num2):
    result=[]
    for i in num1:
        if i in num2:
            result.append(i)
            num2.remove(i)

    return result

num1 = [1,2,2,1] 
num2 = [2,2]

print(intersection(num1,num2))