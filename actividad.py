import random
import sqlite3


opciones = ["piedra", "papel", "tijera"]
numeros = {"1": "piedra", "2": "papel", "3": "tijera"}
salir = False


def mostrar_resumen():
    with sqlite3.connect("partidas.db") as conexion:
        conexion.execute(
            """
            CREATE TABLE IF NOT EXISTS partidas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                jugada TEXT NOT NULL,
                computadora TEXT NOT NULL,
                resultado TEXT NOT NULL
            )
            """
        )
        partidas = conexion.execute(
            "SELECT nombre, resultado FROM partidas"
        ).fetchall()

    print("\n--- Resumen de partidas ---")
    if not partidas:
        print("Todavía no hay partidas guardadas.")
        return

    victorias_jugadores = sum(
        resultado != "Empate" and resultado != "Ganó la computadora"
        for _, resultado in partidas
    )
    empates = sum(resultado == "Empate" for _, resultado in partidas)
    victorias_computadora = sum(
        resultado == "Ganó la computadora" for _, resultado in partidas
    )

    print(f"Partidas jugadas: {len(partidas)}")
    print(f"Victorias de jugadores: {victorias_jugadores}")
    print(f"Victorias de la computadora: {victorias_computadora}")
    print(f"Empates: {empates}")


while not salir:
    print("\n--- Piedra, papel o tijera ---")
    print("1. Empezar una partida")
    print("2. Ver resumen de partidas")
    print("3. Salir")
    opcion = input("Elegí una opción: ")

    if opcion == "2":
        mostrar_resumen()
        continue
    elif opcion == "3":
        print("¡Gracias por jugar!")
        break
    elif opcion != "1":
        print("Esa opción no vale.")
        continue

    nombre = input("¿Cómo te llamas? ").strip()
    while not nombre:
        nombre = input("Escribí tu nombre: ").strip()

    while True:
        jugada = input(
            "\nElegí: 1. Piedra, 2. Papel, 3. Tijera: "
        ).strip().lower()
        jugada = numeros.get(jugada, jugada)

        while jugada not in opciones:
            print("Esa opción no vale.")
            jugada = input("Elegí piedra, papel o tijera: ").strip().lower()
            jugada = numeros.get(jugada, jugada)

        computadora = random.choice(opciones)
        print(f"\n{nombre}: {jugada}")
        print(f"Computadora: {computadora}")

        if jugada == computadora:
            resultado = "Empate"
        elif (
            (jugada == "piedra" and computadora == "tijera")
            or (jugada == "papel" and computadora == "piedra")
            or (jugada == "tijera" and computadora == "papel")
        ):
            resultado = f"Ganó {nombre}"
        else:
            resultado = "Ganó la computadora"

        print(resultado)

        with sqlite3.connect("partidas.db") as conexion:
            conexion.execute(
                """
                CREATE TABLE IF NOT EXISTS partidas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    jugada TEXT NOT NULL,
                    computadora TEXT NOT NULL,
                    resultado TEXT NOT NULL
                )
                """
            )
            conexion.execute(
                """
                INSERT INTO partidas (nombre, jugada, computadora, resultado)
                VALUES (?, ?, ?, ?)
                """,
                (nombre, jugada, computadora, resultado),
            )

        print("La partida quedó guardada.")
        print("\n¿Qué querés hacer?")
        print("1. Jugar de nuevo")
        print("2. Ingresar un nuevo jugador")
        print("3. Empezar una nueva partida")
        print("4. Ver resumen de partidas")
        print("5. Salir")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            continue
        elif opcion == "2":
            nombre = input("¿Cómo se llama el nuevo jugador? ").strip()
            while not nombre:
                nombre = input("Escribí el nombre del nuevo jugador: ").strip()
        elif opcion == "3":
            break
        elif opcion == "4":
            mostrar_resumen()
            break
        elif opcion == "5":
            print("¡Gracias por jugar!")
            salir = True
            break
        else:
            print("Esa opción no vale. Vamos a empezar otra partida.")
            break
