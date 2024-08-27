from dataclasses import dataclass


class Person:
    def __init__(self, name):
        self.name = name


x = Person('pedro')


@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


item = InventoryItem('coin', 2.5, 10)
