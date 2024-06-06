s = "anagram"
t = "nagaram"
sum1 = []
sum2 = []
if(len(s) == len(t)):
    
    for i,j in zip(s,t):
        sum1.append(i)
        sum2.append(j)
        
    sum1.sort()
    sum2.sort()
    if(sum1==sum2):
        print("true")
    else:
        print("false")
else:
    print("false")
    
    
    
