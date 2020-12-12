class Gas_station:
    def __init__(self):
        self.diesel = 1.82
        self.gasoline = 0.99
        self.oil = 15
        self.amount_fuel = 0
        self.amount_oil = 0

    def ref_fuel(self, which, how_much_fuel):
        self.which = which
        self.how_much_fuel = how_much_fuel
        if self.which == "diesel":
            self.amount_fuel = self.how_much_fuel * self.diesel
            print("You have to pay " + str(self.amount_fuel) + "$ for", self.how_much_fuel, "liters", self.which)
        elif self.which == "gasoline":
            self.amount_fuel = self.how_much_fuel * self.gasoline
            print("You have to pay " + str(self.amount_fuel) + "$ for", self.how_much_fuel, "liters", self.which)


    def ref_oil(self,how_much_oil):
        self.how_much_oil = how_much_oil
        self.amount_oil = self.how_much_oil * self.oil
        print("You have to pay " + str(self.amount_oil) + "$ for", self.how_much_oil, "liters oil")
