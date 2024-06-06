def SumOfDigit(n):
    if n<=9:
        return n
    else:
        return (n%10)+SumOfDigit(n//10)

print(SumOfDigit(56))