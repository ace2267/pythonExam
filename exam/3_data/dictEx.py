# 키-값 형식을 갖는 켈렉션
scores = {"aaa": 90, "bbbb": 85, "cccc": 80}
v = scores["aaa"]   # 특정 요소 읽기
print(v)
scores["aaa"] = 88  # 쓰기
print(scores)

# 다양한  경로에서 dict 생성
# 1. Tuple List로부터 dict 생성
persons = [('kim', 30), ('hong', 35), ('kang', 25)]
mydict = dict(persons)
age = mydict["hong"]
print(age)   # 35
# 2. Key=Value 파라미터로부터 dict 생성
scores = dict(a=80, b=90, c=85)
print(scores['b'])  # 90

# 추가,수정,삭제,읽기
scores = {"aaa": 90, "bbb": 85, "ccc": 80}
print(scores)
scores["bbb"] = 88   # 수정
scores["ccc"] = 95   # 추가
del scores["aaa"]
print(scores)

scores = {"aaa": 90, "vvv": 85, "ccc": 80}

for key in scores:
    val = scores[key]
    print("%s : %d" % (key, val))

# 유용한 메서드
scores = {"aaa": 90, "bbb": 85, "ccc": 80}

# keys
keys = scores.keys()
for k in keys:
    print(k)

# values
values = scores.values()
for v in values:
    print(v)

scores = {"aaa": 90, "bbb": 85, "ccc": 80}

items = scores.items()
print(items)
# 출력: dict_items([('aaa', 85), ('bbb', 80), ('ccc', 90)])

# dict_items를 리스트로 변환할 때
itemsList = list(items)
print(itemsList)
