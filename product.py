class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def display(self) -> str:
        return f"Product(name='{self.name}', price={self.price:.2f}, quantity={self.quantity})"

    def update_quantity(self, new_quantity: int):
        new_q = int(new_quantity)
        if new_q < 0:
            raise ValueError("Cantitatea nu poate fi negativă.")
        self.quantity = new_q

    def total_value(self) -> float:
        return self.price * self.quantity

    def __repr__(self):
        return self.display()
