# 빈클래스
class Myclass:
    pass

# 클래스멤버
    #   메서드(method), 속성(property), 클래스 변수(class variable), 인스턴스 변수(instance variable), 초기자(initializer), 소멸자(destructor)

# 메서드
class Rectangle:
    count = 0  # 클래스 변수

    # 초기자(initializer)
    def __init__(self, width, height):
        # self.* : 인스턴스변수
        self.width = width
        self.height = height
        Rectangle.count += 1

    # 메서드
    def calcArea(self):
        area = self.width * self.height
        return area

    # private 메서드
    def __internalRun(self):
        pass

# 클래스변수 - 메서드 밖에 존재하는 변수, 하나의 클래스에 하나만 생성 , Rectangle.count

# 인스턴스변수 - 인스턴스마다 생성 , self.width

# python 기본이 public , 내부사용하는 변수는 _ 붙임(관례).

# 초기자

# 정적메서드 와 클래스 메서드
