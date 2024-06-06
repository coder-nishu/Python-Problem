# #1
# d = [181,178,87,192]
# print(type(d))
# def reversemake(lists):
#     lists.sort()
#     print(lists)
# reversemake(d)

# def reversebubblesort(lists):
#     for i in range(len(lists)):
#         for j in range(i+1,len(lists)):
#             if (lists[i] >= lists[j]):
#                 lists[i],lists[j] = lists[j],lists[i]
                
#     print(lists)
# reversebubblesort(d)

# #2
# k = [1001,1002,1003,1004,1005]
# v = ["usa" ,"canada" , "china" , "japan" , "Uk" ]
# dic = {}
# for i in range(5):
#     dic[k[i]] = v[i]
# print(dic) 

# # st = "I am nishat.you are hafiz.he is anjum"
# # x = st.split(" ")
# # print(x)

# #3
# value1 = [1,2,3,4,5,6,7,8,9]
# value2 = [1,2,3]
# for item in value1:
#     if item == 5:
#         continue
#     print("break")
#     for item2 in value2:
#         print(item,item2)

# #4
# def grade_result(score):
#     grade_mapping = {
#         'A': range(90, 101),
#         'B': range(80, 90),
#         'C': range(70, 80),
#         'D': range(60, 70),
#         'F': range(0, 60)
#     }
#     for grade, score_range in grade_mapping.items():
#         if score in score_range:
#             return grade

# # Example usage
# student_scores = [85, 92, 78, 60, 45]
# for score in student_scores:
#     print(f"Score: {score}, Grade: {grade_result(score)}")

# #5
# def calWaiver():
#     fee = float(input("Enter ur semester fee:"))
#     results = float(input("Enter ur res:"))
#     if results >= 3.50:
#         print("your waiver is 20% & waiver amount:",fee*0.2)
#     elif results>=3.00 and results < 3.50:
#         print("your waiver is 10% & waiver amount:",fee*0.1)
# calWaiver()


# #6
# n = []
# i = 1
# while i<= 100:
#     n.append(i)
#     i+=2
# print(n)

# list1 = [1,2,3]
# list2 = [1,5,6,3,3,3,3,7,8]
# new_list = []
# for i in list1:
#     for j in list2:
#         if i == j:
#             if i not in new_list:
#                 new_list.append(i)
# print(new_list)
  
# #7
# lists = ['india', 'china', 'nepal', 'myanmar']

# for i in range( len(lists) - 1):
#     print(lists[i], end=' ,')            
            

# #8
# f = [1, 2, 3]
# s = [2,2,2,2, 4, 5]
# common = []

# # for i in f:
# #     if i in s:
# #         common.append(i)

# # print(common)


# #9
# n = input("enter element:").split()
# newlist = []

# if len(n) <= 2:
#     print("Not possible")
# else:
#     for i in range(1,len(n)-1):
#       newlist.append(n[i])
#     print(newlist)


# #10
# add = 0
# n = int(input())
# for i in range(n):
#     x, y = input().split()
#     x = int(x)
#     y = int(y)
#     for j in range(x, (x + (y * 2))):
#         if j % 2 != 0:
#             add = add + j
#     print(add)

# #11
# lists = ['shikha' ,'haua','Muzam', "01919034469"]
# lenth = 0
# count_c = 0
# vowel = ['a', 'e','i','o','u']
# a = ['A','E','I','O','U']
# for i in range(len(a)):
#     if vowel[i] == a[i]:
#         print("same")
#     else:
#         print("not same")

# for i in lists:
#     lenth += len(i)
#     for j in i:
#         if j in vowel:
#             count_c += 1
# print(lenth,count_c)


# #12
# dict = { }
# for i in range(20,61):
#     if i%2 == 0 or i %5 ==0:
#         dict[i] = i+7
#     elif i%5 == 0:
#         dict[i] = i+2
#     elif i%2 == 0:
#          dict[i] = i+5
        
# print(dict)
# print(len(dict))

#Q-2
# fn = "Ummey"
# ln = "Ayman"
# id ="3215678"
# password = ' '
# password += fn[:3].upper()
# password += str(ord(ln[-1:-3]))
# password += str(id)


# def grade_result(score):
#     grade_info = {
#         'A': range(90, 101),
#         'B': range(80, 90),
#         'C': range(70, 80),
#         'D': range(60, 70),
#         'F': range(0, 60)
#     }
#     for grade, grade_range in grade_info.items():
#         if score in grade_range:
#             print(f"your grade: {grade}")
# grade_result(82)

# l = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# new = []
# for i in range(len(l)):
#     temp = []
#     for j in range(len(l[0])):
#         temp.append(l[j][i])
#     new.append(temp)
# print(new)

# l = [1,2,3,4,5,2]
# new = []
# for i in l:
#     if l.count(i) < 2:
#         new.append(i)
# print(new)     

s = "nishat"
x = s.reverse()
