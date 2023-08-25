# Corregir tamaño de la lista
productsWeb = [
    {"name": "Product 1", "price": 5, "stock": 100},
    {"name": "Product 2", "price": 5, "stock": 100},
    {"name": "Product 3", "price": 5, "stock": 100},
    {"name": "Product 4", "price": 5, "stock": 100},
]

for product in productsWeb:
    if product["name"] == "Product 2":
        # Eliminar diferencia entre espacios y tabuladores
        print("Hola producto 2")
    print(product)
