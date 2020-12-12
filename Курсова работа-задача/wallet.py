class Wallet:
    def __init__(self, how_much_in_card, how_much_in_cash):
        self.card = how_much_in_card
        self.cash = how_much_in_cash

    def pay(self, method):
        self.method = method
        self.money = 0
        if self.method == "card":
            self.money = self.card
        elif self.method =="cash":
            self.money = self.cash
