from itertools import product, permutations
import tkinter as tk

# Planificación de Ataques en el juego Risk
# Contexto:
# En el juego de mesa Risk, eres el líder de un ejército que planea conquistar territorios enemigos.
# Imagina que has apostado quién paga la cena y tienes que ganar a toda costa porque si te toca pagar a ti acabáis en un kebab y eso no es sano.
# Para ganar, debes decidir:
# 1. Qué combinación de tropas utilizarás para el ataque.
# 2. El orden en que atacarás los territorios enemigos.
# 3. Optimizar tus movimientos mientras cumples restricciones de tropas disponibles.

def generate_combinations(max_points, troop_costs):
    """
    Genera todas las combinaciones posibles de tropas respetando los recursos disponibles.
    Debe incluir al menos una unidad de cada tipo de tropa.
    """
    combinations = []
    for infantry, cavalry, artillery in product(range(max_points + 1), repeat=3):
        if infantry * troop_costs['infantry'] + cavalry * troop_costs['cavalry'] + artillery * troop_costs['artillery'] <= max_points:
            if infantry > 0 and cavalry > 0 and artillery > 0:  # Restricción extra
                combinations.append((infantry, cavalry, artillery))
    return combinations

def generate_permutations(territories):
    """
    Genera todas las permutaciones posibles del orden de ataque a los territorios enemigos.
    """
    return list(permutations(territories))

def calculate_force(troops, troop_strength):
    """
    Calcula la fuerza total de un ejército dado.
    """
    infantry, cavalry, artillery = troops
    return (infantry * troop_strength['infantry'] +
            cavalry * troop_strength['cavalry'] +
            artillery * troop_strength['artillery'])

def assign_troops_to_terrain(territory_type, troops):
    """
    Asigna las tropas en función del tipo de terreno del territorio.
    Ejemplo: usar más caballería en terrenos planos.
    """
    if territory_type == "plano":
        # Priorizar caballería
        return (troops[0] // 2, troops[1] + troops[0] // 2, troops[2])
    elif territory_type == "montañoso":
        # Priorizar artillería
        return (troops[0], troops[1], troops[2] + troops[0] // 2)
    else:
        # Sin prioridad específica
        return troops

def optimize_combinations(territories, troop_combinations, troop_strength):
    """
    Encuentra la combinación de tropas que maximiza las conquistas.
    """
    best_combination = None
    max_conquered = 0

    for combination in troop_combinations:
        total_force = calculate_force(combination, troop_strength)
        conquered = 0
        for territory in sorted(territories):
            if total_force >= territory:
                total_force -= territory
                conquered += 1
            else:
                break

        if conquered > max_conquered:
            max_conquered = conquered
            best_combination = combination

    return best_combination, max_conquered

def plan_attacks(territories, troop_combinations, troop_strength, terrain_types, prioritize_weakest=False):
    """
    Encuentra la mejor estrategia para conquistar los territorios dados las combinaciones de tropas.
    Si prioritize_weakest es True, ordena los territorios de más débil a más fuerte.
    """
    if prioritize_weakest:
        sorted_territories = sorted(zip(territories, terrain_types), key=lambda x: x[0])
    else:
        sorted_territories = list(zip(territories, terrain_types))

    best_strategy = None
    max_territories_conquered = 0

    for combination in troop_combinations:
        total_force = calculate_force(combination, troop_strength)
        conquered = 0
        for territory, terrain in sorted_territories:
            adjusted_troops = assign_troops_to_terrain(terrain, combination)
            adjusted_force = calculate_force(adjusted_troops, troop_strength)
            if total_force >= territory:
                total_force -= territory
                conquered += 1
            else:
                break

        if conquered > max_territories_conquered:
            max_territories_conquered = conquered
            best_strategy = combination

    return best_strategy, max_territories_conquered

def represent_board(enemy_territories):
    """
    Representa el tablero con la estructura de datos de territorios enemigos.
    """
    board = {f"Territorio {i + 1}": defense for i, defense in enumerate(enemy_territories)}
    return board

def show_board_in_window(board, troop_strength):
    """
    Muestra el tablero en una ventana gráfica con formas, colores y figuras necesarias para derrotar cada territorio.
    """
    root = tk.Tk()
    root.title("Tablero de juego")
    canvas = tk.Canvas(root, width=600, height=500, bg="white")
    canvas.pack()

    x, y = 50, 50
    for i, (territory, defense) in enumerate(board.items()):
        color = "green" if defense <= 5 else "yellow" if defense <= 10 else "red"
        required_infantry = defense // troop_strength['infantry']
        required_cavalry = defense // troop_strength['cavalry']
        required_artillery = defense // troop_strength['artillery']

        canvas.create_rectangle(x, y, x + 100, y + 50, fill=color, outline="black")
        canvas.create_text(x + 50, y + 15, text=f"{territory}", font=("Arial", 10), fill="black")
        canvas.create_text(x + 50, y + 35, text=f"Def: {defense}", font=("Arial", 10), fill="black")
        canvas.create_text(x + 150, y + 25, 
                           text=f"Inf: {required_infantry}, Cav: {required_cavalry}, Art: {required_artillery}", 
                           font=("Arial", 10), fill="black")
        y += 70
        if y > 400:
            y = 50
            x += 250

    root.mainloop()

def main():
    # Entrada de datos
    print("Bienvenido al planificador de ataques del juego Risk")
    max_points = int(input("Ingresa los puntos máximos disponibles para tropas (ejemplo: 20): "))

    print("Configura los costos y la fuerza de cada tipo de tropa:")
    troop_costs = {
        'infantry': int(input("Costo de una unidad de infantería (ejemplo: 1): ")),
        'cavalry': int(input("Costo de una unidad de caballería (ejemplo: 3): ")),
        'artillery': int(input("Costo de una unidad de artillería (ejemplo: 5): "))
    }

    troop_strength = {
        'infantry': int(input("Fuerza de una unidad de infantería (ejemplo: 1): ")),
        'cavalry': int(input("Fuerza de una unidad de caballería (ejemplo: 3): ")),
        'artillery': int(input("Fuerza de una unidad de artillería (ejemplo: 5): "))
    }

    num_territories = int(input("Número de territorios enemigos (ejemplo: 3): "))
    enemy_territories = []
    terrain_types = []
    for i in range(num_territories):
        defense = int(input(f"Defensa del territorio {i + 1} (ejemplo: 10): "))
        terrain_type = input(f"Tipo de terreno del territorio {i + 1} (plano/montañoso): ")
        enemy_territories.append(defense)
        terrain_types.append(terrain_type)

    # Representar el tablero
    board = represent_board(enemy_territories)

    # Generar combinaciones de tropas
    troop_combinations = generate_combinations(max_points, troop_costs)

    # Optimizar combinaciones
    best_combination, max_conquered = optimize_combinations(enemy_territories, troop_combinations, troop_strength)

    print("\n==========================")
    print("Optimización de tropas:")
    print("Mejor Combinación de Tropas:", best_combination)
    print("Máximo de Territorios Conquistados:", max_conquered)
    print("==========================")

    # Generar permutaciones de territorios
    attack_orders = generate_permutations(enemy_territories)

    # Elegir la mejor estrategia con prioridad a territorios más débiles
    best_strategies = []

    for order in attack_orders:
        best_strategy, conquered = plan_attacks(order, troop_combinations, troop_strength, terrain_types, prioritize_weakest=True)
        best_strategies.append((order, best_strategy, conquered))

    # Ordenar estrategias por territorios conquistados
    best_strategies.sort(key=lambda x: x[2], reverse=True)

    # Imprimir el mejor resultado
    best_order, best_troops, conquered = best_strategies[0]

    print("\n==========================")
    print("Mejor Orden de Ataque:", best_order)
    print("Mejor Combinación de Tropas (Estrategia):", best_troops)
    print("Territorios Conquistados en Estrategia:", conquered)
    print("==========================")

    # Submenú
    while True:
        print("\n¿Qué quieres hacer ahora?")
        print("1. Mostrar el tablero en una ventana.")
        print("2. Salir.")
        choice = input("Selecciona una opción (1 o 2): ")

        if choice == "1":
            show_board_in_window(board, troop_strength)
        elif choice == "2":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()
