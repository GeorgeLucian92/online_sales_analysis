from typing import List, Optional
from product import Product

class ProductManager:
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product):
        existing = self.find_product(product.name)
        if existing:
            existing.quantity += product.quantity
        else:
            self.products.append(product)

    def find_product(self, name: str) -> Optional[Product]:
        name_lower = name.strip().lower()
        for p in self.products:
            if p.name.strip().lower() == name_lower:
                return p
        return None

    def remove_product_by_name(self, name: str) -> bool:
        p = self.find_product(name)
        if p:
            self.products.remove(p)
            return True
        return False

    def update_product_quantity(self, name: str, new_quantity: int) -> bool:
        p = self.find_product(name)
        if p:
            p.update_quantity(new_quantity)
            return True
        return False

    def list_products(self) -> List[Product]:
        return list(self.products)

    def display_all(self) -> str:
        if not self.products:
            return "Nu sunt produse în inventar."
        lines = [p.display() for p in self.products]
        return "\n".join(lines)

    def total_inventory_value(self) -> float:
        total = 0.0
        for p in self.products:
            total += p.total_value()
        return total
