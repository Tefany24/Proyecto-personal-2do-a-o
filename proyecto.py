# Definición de funciones

# Menú del restaurante con platillos y precios
menu = [
    {"nombre": "Pupusas", "precio": 0.75},
    {"nombre": "Burritos", "precio": 7},
    {"nombre": "Tamales", "precio": 1},
    {"nombre": "Carne", "precio": 3.50},
    {"nombre": "Pollo", "precio": 3}
]

# Función para mostrar el menú
def mostrar_menu():
    print("\nMenú del Restaurante:")
    for i, platillo in enumerate(menu):
        print(f"{i + 1}. {platillo['nombre']} - ${platillo['precio']}")