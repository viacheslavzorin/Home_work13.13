from item import Item

item1 = Item("Смартфон", 20, 10000)
item2 = Item("Ноутбук", 5, 20000)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

Item.pay_rate = 0.8  # устанавливаем новый уровень цен
item1.apply_discount()
print(int(item1.price))
print(item2.price)

print(Item.instances)







