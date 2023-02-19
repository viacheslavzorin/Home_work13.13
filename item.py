

class Item:
    instances = []
    num_of_item = 0
    pay_rate = 0.85

    def __init__(self, product, quanity, price):
        self.product = product
        self.quanity = quanity
        self.price = price
        self.instances.append(self)

        Item.num_of_item += 1

    def calculate_total_price(self):
        return self.quanity * self.price

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price



