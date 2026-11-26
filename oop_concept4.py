class Comet:
    def __init__(self, name, current_year, next_year, period):
        self.name = name
        self.current_year = current_year
        self.next_year = next_year
        self.period = period

    def show_Info(self):
        print("comet: ", self.name)
        print("current_year: ", self.current_year)
        print("next_year: ", self.next_year)
        print("average period: ", self.period)

c1 = Comet("Halley", 1986, 2061, 76)
c1.show_Info()