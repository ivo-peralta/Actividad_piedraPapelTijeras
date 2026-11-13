# Actividad_piedraPapelTijeras
La actividad que propusieron los chicos en clase

Requisito	Estado
Definir clases	No cumple: no hay ninguna declaración class.
Crear y utilizar objetos propios	No cumple: utiliza variables, una función y bucles.
Separar las clases en archivos	No cumple: todo el código está en actividad.py.
Distribuir responsabilidades	Falta: los menús, las reglas del juego y las operaciones de SQLite están mezclados.


Una organización posible —si no exigiste clases específicas— sería:
- jugador.py: clase Jugador, con el nombre y los comportamientos correspondientes.
- juego.py: clase Juego, responsable de las jugadas y de determinar el resultado.
- base_datos.py: clase responsable de guardar partidas y consultar estadísticas.
- main.py: punto de entrada que crea los objetos y coordina su uso.
