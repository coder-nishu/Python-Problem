#map(function,iterables)
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

#class  problem
x = list(map(int,input("Enter integers:").split(' ')))
print(x)