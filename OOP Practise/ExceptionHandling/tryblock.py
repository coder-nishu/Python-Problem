def division(a,b):
    try:
        result = a/b
    except ZeroDivisionError as e:
        print("The exception is :",e)
   


division(5,0)
print("hello world")