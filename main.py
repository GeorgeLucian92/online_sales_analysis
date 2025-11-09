from product import Product
from product_manager import ProductManager

def seed_products(pm: ProductManager):
    pm.add_product(Product("Tricou", 49.99, 10))
    pm.add_product(Product("Pantaloni", 129.50, 5))
    pm.add_product(Product("Sapca", 29.90, 20))
    pm.add_product(Product("Sosete (pereche)", 9.99, 50))
    pm.add_product(Product("Geaca", 399.00, 2))

def main():
    pm = ProductManager()
    seed_products(pm)
    print("=== Produse în inventar ===")
    print(pm.display_all())
    print(f"Valoarea totală a inventarului: {pm.total_inventory_value():.2f} RON")

if __name__ == "__main__":
    main()
