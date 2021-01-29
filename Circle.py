import math

class Circle:
    def __init__(self, radius = 1):
        self.radius = radius
        # self.__radius = radius 인 경우, __ 즉, 은닉을 하기 때문에 radius가 출력이 안된다.

    #def getRadius(self):
        #return self.__radius
    
    def getPerimeter(self):
        return 2 * self.radius *math.pi

    def getArea(self):
        return self.radius * self.radius * math.pi
