def fibonacci(n):
    if n <= 1:
        return n
        # base case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
        # recursive case

for i in range(5):
    print(fibonacci(i), end=", ")

# 0,1,2,3,4