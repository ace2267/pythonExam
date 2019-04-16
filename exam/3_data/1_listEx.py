# list- 동적배열, 다양한 요소
a = ["AB", 10, False]

# index
print(a[0])
print(a[1])
print(a[-1])

# slicing
print(a[1:2]) # index 1~1
print(a[1:3]) # index 1~2
print(a[0:]) # index 0~2
print(a[:3]) # index 0~2

# item add, mod, del
a.append(11.1) # add
print(a)
a[0] =2 # mod
print(a)
del a[2] # del
print(a)

# 병합 , 반복
a = [1,2,3]
b = [4,5]
print(a+b)
print(a*3)

# 검색
mylist = "this is a book that is a pencil".split()
print(mylist.index('book'))
print(mylist.count('is'))

# List Comprehension
list = [n ** 2 for n in range(10) if n % 3 == 0]
print(list)
