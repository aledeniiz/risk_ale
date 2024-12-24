# Risk Game Planner

## Descripción

Este proyecto es una herramienta diseñada para optimizar la planificación de ataques en el juego de mesa **Risk**. Permite calcular las mejores combinaciones de tropas y estrategias de ataque para conquistar territorios enemigos, respetando las limitaciones de recursos y fuerzas de defensa. Además, incluye una representación visual del tablero de juego con datos adicionales, como la cantidad de unidades necesarias para conquistar cada territorio.

## Funcionalidades

1. **Generación de combinaciones de tropas:**

   - Calcula todas las combinaciones posibles de tropas respetando los recursos disponibles.
   - Garantiza que haya al menos una unidad de cada tipo de tropa (infantería, caballería, artillería).

2. **Generación de permutaciones de ataque:**

   - Genera todas las posibles órdenes de ataque a los territorios enemigos.

3. **Optimización de tropas:**

   - Encuentra la combinación de tropas que maximiza el número de territorios conquistados con los recursos disponibles.

4. **Planificación de ataques:**

   - Determina la mejor estrategia considerando el tipo de terreno de cada territorio.
   - Prioriza atacar territorios más débiles si se configura esta opción.

5. **Representación visual del tablero:**

   - Muestra un tablero interactivo en una ventana gráfica.
   - Representa cada territorio con colores según su nivel de defensa.
   - Incluye datos sobre las unidades necesarias (infantería, caballería, artillería) para conquistar cada territorio.

## Requisitos

- Python 3.8 o superior.
- Biblioteca `tkinter` (incluida por defecto en Python).

## Cómo usar

1. **Ejecutar el programa:**

   - Corre el archivo `risk_game_planner.py` en un entorno compatible con Python.

2. **Ingresar los datos iniciales:**

   - Define los puntos máximos disponibles para tropas.
   - Configura los costos y la fuerza de cada tipo de tropa.
   - Especifica el número de territorios enemigos, su nivel de defensa y el tipo de terreno (plano o montañoso).

3. **Resultados:**

   - El programa mostrará la mejor combinación de tropas y la estrategia de ataque más efectiva.
   - Opcionalmente, se puede visualizar un tablero interactivo con información detallada de los territorios.

## Representación visual

El tablero se muestra en una ventana gráfica, donde:

- Los territorios se representan con colores:
  - **Verde:** Defensa baja.
  - **Amarillo:** Defensa media.
  - **Rojo:** Defensa alta.
- Se muestran los datos de defensa y la cantidad de tropas necesarias para cada territorio.

