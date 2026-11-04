import sqlite3
import random

opciones = ["piedra", "papel", "tijera"]

nombre = input("¿Cómo te llamas? ")

jugada = input("Elige piedra, papel o tijera: ").lower()
while jugada not in opciones:
    jugada = input("Esa opción no vale. Elige piedra, papel o tijera: ").lower()

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
        "INSERT INTO partidas (nombre, jugada, computadora, resultado) VALUES (?, ?, ?, ?)",
        (nombre, jugada, computadora, resultado),
    )

print("La partida quedó guardada.")
