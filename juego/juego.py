import sys
import time

# Posición inicial del personaje
personaje = {"x": 0, "y": 0}

# Inventario inicial
inventario = []

# Funciones para las acciones
def mover_personaje(tecla):
    if tecla == "w":
        personaje["y"] += 1
        print(f"Te moviste hacia arriba. Nueva posición: {personaje}")
    elif tecla == "s":
        personaje["y"] -= 1
        print(f"Te moviste hacia abajo. Nueva posición: {personaje}")
    elif tecla == "a":
        personaje["x"] -= 1
        print(f"Te moviste hacia la izquierda. Nueva posición: {personaje}")
    elif tecla == "d":
        personaje["x"] += 1
        print(f"Te moviste hacia la derecha. Nueva posición: {personaje}")

def interactuar():
    print("Has interactuado con un objeto o personaje cercano.")

def abrir_menu():
    print("Menú del juego abierto. Pulsa 'ESC' nuevamente para cerrarlo.")
    time.sleep(2)  # Simula la apertura del menú
    print("Menú cerrado.")

def abrir_inventario():
    print("Inventario abierto:")
    if inventario:
        for i, item in enumerate(inventario, start=1):
            print(f"{i}. {item}")
    else:
        print("Tu inventario está vacío.")
    time.sleep(2)  # Simula la apertura del inventario
    print("Inventario cerrado.")

# Función principal
def juego():
    print("¡Bienvenido al juego! Usa W, A, S, D para moverte. F para interactuar, E para inventario, y ESC para el menú.")
    while True:
        tecla = input("Presiona una tecla (WASD para moverse, F para interactuar, E para inventario, ESC para menú, Q para salir): ").lower()
        
        if tecla == "w" or tecla == "a" or tecla == "s" or tecla == "d":
            mover_personaje(tecla)
        elif tecla == "f":
            interactuar()
        elif tecla == "e":
            abrir_inventario()
        elif tecla == "esc":
            abrir_menu()
        elif tecla == "q":
            print("¡Gracias por jugar! Saliendo del juego...")
            sys.exit()
        else:
            print("Tecla no reconocida. Intenta nuevamente.")

# Iniciar el juego
if __name__ == "__main__":
    juego()
