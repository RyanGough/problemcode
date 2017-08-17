

class DiscountCalculator:

    def discount(self, item):
        if item == "apple":
            return 10

        if item == "pear":
            return 20

        return 0


class Checkout:

    discount_calc = DiscountCalculator()
    prices = {
        "apple": 199,
        "pear": 185,
        "orange": 150
    }
    items = []

    def scan(self, item):
        self.items.append(item)

    def reset(self):
        self.items = []

    def cost(self):
        total = sum([self.prices[x] for x in self.items])
        discount = sum([self.discount_calc.discount(x) for x in self.items])
        return total - discount
