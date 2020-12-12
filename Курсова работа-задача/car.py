from gas_station import Gas_station
from wallet import Wallet
print_line = (lambda:print (f"======================================="))
class Car:
    def __init__(self, what_fuel, tank_volume, how_much_fuel, how_much_oil):
        self.what_fuel = what_fuel
        self.how_fuel = how_much_fuel
        self.how_oil = how_much_oil
        self.tank_volume = tank_volume
        self.oil_tank = 5
        print("You have a", self.what_fuel,"car with", self.tank_volume, "liters tank")
        print("Fuel:", self.how_fuel, "liters")
        print("Oil:", self.how_oil, "liters")
        print_line()

    def driving(self, how_many_km):
        if self.what_fuel == "diesel":
           self.how_many_km = how_many_km
           if self.how_fuel >= (self.how_many_km * 0.06) and self.how_oil >= (self.how_many_km * 0.001):
              self.how_fuel -= self.how_many_km * 0.06
              self.how_oil -= self.how_many_km * 0.001
              print("Driving for", self.how_many_km, "kilometers on", self.what_fuel.capitalize() + ".")
              print("Fuel left:",self.how_fuel,"liters")
              print("Oil left",self.how_oil,"liters")
              print_line()
           else:
              print("Your car won't go that far :D")
              print_line()
        elif self.what_fuel == "gasoline":
           self.how_many_km = how_many_km
           if self.how_fuel >= (self.how_many_km * 0.10) and self.how_oil >= (self.how_many_km * 0.001):
              self.how_fuel -= self.how_many_km * 0.10
              self.how_oil -= self.how_many_km * 0.001
              print("Driving for", self.how_many_km, "kilometers on", self.what_fuel.capitalize() + ".")
              print("Fuel left:",round(self.how_fuel, 2),"liters")
              print("Oil left",round(self.how_oil, 2),"liters")
              print_line()
           else:
              print("Your car won't go that far :D")
              print_line()
        else:
           print("There is no fuel like: " + str(self.what_fuel))
           print_line()

    def ref_fuel(self,how_much):
        self.how_much = how_much
        self.g = Gas_station()
        if self.how_much <= (self.tank_volume - self.how_fuel):
            self.how_fuel += self.how_much
            print("Refueling to", round(self.how_fuel, 2), "liters from", round((self.how_fuel - self.how_much), 2))
            self.g.ref_fuel(self.what_fuel, self.how_much)
            print_line()
        else:
            print("You don't have enought space for that much fuel.")
            print_line()

    def ref_oil(self, how_much_oil):
        self.how_much_oil = how_much_oil
        if self.how_much_oil <= (self.oil_tank - self.how_oil):
            self.how_oil += self.how_much_oil
            print("Refueling to", round(self.how_oil, 2), "liters from", round((self.how_oil - self.how_much_oil), 2))
            self.g.ref_oil(self.how_much_oil)
            print_line()
        else:
            print("You don't have enought space for that much oil.")
            print_line()

    def pay(self, how_much_card, how_much_cash, method):
        self.how_much_card = how_much_card
        self.how_much_cash = how_much_cash
        self.method = method
        self.w = Wallet(self.how_much_card, self.how_much_cash)
        self.w.pay(self.method)
        if self.w.money >= (self.g.amount_fuel + self.g.amount_oil):
            self.w.money -= (self.g.amount_fuel + self.g.amount_oil)
            print("You have", str(self.w.money) + "$ left.")
            print_line()
            print_line()
        else:
            print("You don't have enough money\nBut we already filled your tank\nI'm calling the police!")
            print_line()
            print_line()



