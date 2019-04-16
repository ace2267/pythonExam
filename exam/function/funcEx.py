# simple function
def sum(a,b):
    s = a + b
    return s

total = sum(4,4000)

print(total)

# 파라미터 전달 방식
def f(i, mylist):
    i = i +1
    mylist.append(0)

k = 10 # immutable
m = [1,2,3] # mutable

f(k,m)
print(k)
print(m)

# default parameter
def calc(i,j, factor =1):
    return i * j * factor

result = calc(10,100)

print(result)

# named parameter
def report(name, age, score) :
    print(name , score  ,age)

report(age=20,score=30,name="kimsj")

# 가변길이 파라미터
def total(*numbers) :
    tot =0
    for n in numbers :
        tot += n
    return tot

t = total(1,2)
print(t)
t = total(1,2,5,6,2,2)
print(t)

# 복수 리턴값
def calc(*numbers):
    count = 0
    tot = 0
    for n in numbers:
        tot += n
        count += 1
    return count, tot

sum, count   = calc(1,200,33,44)
print(sum, count)
