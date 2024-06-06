def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
lists = [1,2,3,4,5,6,7,8,9,10]
x = list(map(fibonacci,lists))
print(x)
