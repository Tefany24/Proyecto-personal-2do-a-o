# Simulador de Pedidos de un Restaurante

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

# Función para ver el pedido actual
def ver_pedido(pedido):
    if pedido:
        print("\nTu pedido actual:")
        total = 0
        for platillo in pedido:
            print(f"{platillo['nombre']} - ${platillo['precio']}")
            total += platillo['precio']
        print(f"Total del pedido: ${total}")
    else:
        print("\nNo has agregado ningún platillo a tu pedido.")

# Función para finalizar el pedido y calcular el total
def finalizar_pedido(pedido):
    if pedido:
        total = sum(platillo['precio'] for platillo in pedido)
        print(f"\nEl total de tu pedido es: ${total}")
        confirmar = input("¿Quieres confirmar el pedido? (sí/no): ").lower()
        if confirmar == 'sí':
            print("¡Pedido confirmado! ¡Gracias por tu compra!😊")
            return True
        else:
            print("Pedido no confirmado.")
            return False
    else:
        print("\nNo tienes ningún platillo en tu pedido.")
        return False

#Menú interactivo
def mostrar_menú_principal():
    print("\n----Simulador de Pedidos de Restaurante----")
    print("1.Ver menú y hacer pedido.")
    print("2.Ver pedido actual.")
    print("3.finalizar pedido.")
    print("4.Salir.")

# Función principal para ejecutar el simulador de pedidos
def ejecutar_simulador():
    pedido = []
    while True:
        mostrar_menú_principal()
        try:
            opcion = int(input("\nSelecciona una opción: "))
            if opcion == 1:
                agregar_pedido(pedido)
            elif opcion == 2:
                ver_pedido(pedido)
            elif opcion == 3:
                if finalizar_pedido(pedido):
                    break
            elif opcion == 4:
                print("Gracias por usar el simulador. ¡Hasta luego!🤗")
                break
            else:
                print("Opción no válida.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
 
# Ejecutar el simulador
ejecutar_simulador()


