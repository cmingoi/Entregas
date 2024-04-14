import hlf_clases
import hlf_variables
import hlf_funciones

def main():
    print("¡Bienvenido a Batalla Naval!")

    # Inicializar tableros de ambos jugadores
    tablero_jugador = hlf_clases.Tablero("Jugador")
    tablero_maquina = hlf_clases.Tablero("Máquina")
    tablero_jugador.colocar_barcos()
    tablero_maquina.colocar_barcos()

    # Ciclo principal del juego
    while True:
        # Turno del jugador
        print("\nTurno del Jugador:")
        tablero_maquina.imprimir_tablero()
        coordenada_jugador = input("Ingrese coordenada para disparar: ")
        print("El jugador dispara a la coordenada:", coordenada_jugador)
        if not hlf_funciones.validar_coordenada(coordenada_jugador):
            print("Coordenada inválida. Inténtalo de nuevo.")
            continue
        tablero_maquina.disparo_coordenada(coordenada_jugador)
        if hlf_funciones.juego_terminado(tablero_maquina):
            print("¡Has ganado! ¡Felicidades!")
            break

        # Turno de la máquina
        print("\nTurno de la Máquina:")
        tablero_jugador.imprimir_tablero()
        coordenada_maquina = hlf_funciones.generar_coordenada_aleatoria()
        print("La Máquina dispara a la coordenada:", coordenada_maquina)
        tablero_jugador.disparo_coordenada(coordenada_maquina)
        if hlf_funciones.juego_terminado(tablero_jugador):
            print("¡La Máquina ha ganado! ¡Inténtalo de nuevo!")
            break

if __name__ == "__main__":
    main()