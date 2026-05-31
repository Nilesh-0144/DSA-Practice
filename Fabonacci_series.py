def fibonacci(n):
    if n <= 1:
        return n

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b
        print(a,b,end=" ")
    print()

    return b

print("Answer:",fibonacci(5))