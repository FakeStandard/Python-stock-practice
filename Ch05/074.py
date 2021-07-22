# 074 class
class Pig():
    # 建構子
    def __init__(self, name, age, weight):
        self.Name = name
        self.Age = age
        self.Weight = weight
    # 方法

    def Eat(self, n):
        self.Weight += n
        return self.Weight

    def Excreta(self, n):
        self.Weight -= n
        return self.Weight

    def ShowWeight(self):
        return self.Weight


p = Pig('jack', 24, 84)
print(p)

w = p.ShowWeight()
print(w)

w = p.Eat(10)
print(w)

w = p.Excreta(8)
print(w)
