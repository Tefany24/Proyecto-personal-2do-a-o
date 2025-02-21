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

        # Función para agregar un platillo al pedido
def agregar_pedido(pedido):
    mostrar_menu()
    try:
        opcion = int(input("\nSelecciona el número del platillo que deseas agregar: ")) - 1
        if 0 <= opcion < len(menu):
            pedido.append(menu[opcion])
            print(f"Agregado: {menu[opcion]['nombre']} - ${menu[opcion]['precio']}")
        else:
            print("Opción no válida.")
    except ValueError:
        print("Por favor, ingresa un número válido.")