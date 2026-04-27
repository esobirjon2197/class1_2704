# 1-m
class Odam:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def salom(self):
        print("Salom", end=" ")

class Talaba(Odam):
    def salom(self):
        super().salom()
        print("Salom, men talaba")

t1 = Talaba("Sobirjon", 16)
t1.salom()


# 2-m
class Hayvon:
    def __init__(self, nomi):
        self.nomi = nomi

    def ovoz(self):
        print("Ovoz chiqaradi", end=" ")

class Mushuk(Hayvon):
    def ovoz(self):
        super().ovoz()
        print("Miyov")

m1 = Mushuk("Mushuk")
m1.ovoz()

m2 = Hayvon("Mushuk")
m2.ovoz()
