class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img,"j")

    def __add__(self, num2):
        newREAL = self.real + num2.real
        newIMG = self.img + num2.img
        return Complex(newREAL, newIMG)

    def __sub__(self, num2):
        newREAL = self.real - num2.real
        newIMG = self.img - num2.img
        return Complex(newREAL, newIMG)

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(2, 4)
num2.showNumber()

#num3 = num1.add(num2)
#print(num3.showNumber())

num3 = num1 + num2
print(num3.showNumber())

num4 = num3 - num2
print(num4.showNumber())