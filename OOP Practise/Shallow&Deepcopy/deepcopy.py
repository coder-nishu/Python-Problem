import copy
old = [[12,13,14,15],[1,2,3,4,5]]
new = copy.deepcopy(old)
print(old)
print(new)

print("after changing")
old[0][2] = 69
print(old)
print(new)