#inheritance
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop(self):
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("Toyota", "Prius")
print(car1.name)
print(car1.type)



