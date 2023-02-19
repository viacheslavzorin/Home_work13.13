import pytest_cov
from item import Item

#item = Item("Смартфон", 20, 10000)
def test_calculate_total_prise(test_data):
   # item = Item("Смартфон", 10, 10000)
    #pay_rate = 0.85
    assert test_data.calculate_total_price() == 200000
def test_apply_discount(test_data):
    assert test_data.apply_discount() == 8500