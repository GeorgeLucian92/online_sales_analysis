from typing import List
from product import Product
import copy

class Cart:
    def __init__(self):
        self.cart_items: List[Product] = []

    def add_to_cart(self, product: Product, quantity: int = 1):
        if quantity <= 0:
            raise ValueError("Quantity must be > 0")
        name = product.name.strip().lower()
        for p in self.cart_items:
            if p.name.strip().lower() == name:
                p.quantity += quantity
                return
        new_p = copy.deepcopy(product)
        new_p.quantity = int(quantity)
        self.cart_items.append(new_p)

    def total_price(self) -> float:
        total = 0.0
        for p in self.cart_items:
            total += p.price * p.quantity
        return total

    def display_cart(self) -> str:
        if not self.cart_items:
            return "Coșul este gol."
        lines = [f"{p.name} - {p.quantity} buc. x {p.price:.2f} = {p.price * p.quantity:.2f}" for p in self.cart_items]
        lines.append(f"TOTAL: {self.total_price():.2f}")
        return "\n".join(lines)
