#5. List of Lists Concatenation: Given a list of nested lists, write a Python program to concatenate all the sublists into a single flat list.
list1 = [1,2,3,4,"ammu"]
list2 = [6,7,8,9,10]
new_list = list1 + list2
print(new_list)

#another process
list1 = [1,2,3,4,"ammu"]
list2 = [6,7,8,9,10]
list1.extend(list2)
print(list1)
def concat(list1,list2):
    list1.extend(list2)
    return list1
     
print(concat(list1,list2))