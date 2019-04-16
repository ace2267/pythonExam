# tuple - 초기화후 추가 ,갱신, 삭제 불가
t = ("AB", 10, False)
print(t)
t2 = (11,)
print(t2)

# tuple index , slicing
t = (1, 5, 10)
print(t[1])
print(t[-1])
print(t[1:2])
print(t[0:])
print(t[:3])

#tuple 병합, 반복
a= (1,3)
b= (2,4)
print(a+b)
print(b*3)

#tuple 변수할당
name = ("aaaa","bbb")
print(name)
first, last = ("aaaa","bbb")
print(first,",",last)

# 두개의 리스트 zip()시에 생성
a= (1,3)
b= (2,4)
c= zip(a,b)
print(list(c))
