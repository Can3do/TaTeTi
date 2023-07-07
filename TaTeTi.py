tablero =[  "-", "-", "-", #aquí se define al tablero del juego como un array
            "-", "-", "-",
            "-", "-", "-"]

ganador = False # se inicializa la variable para el ganador del juego

combinacionesGanadoras = [{1, 2, 3},{4, 5, 6},{7, 8, 9},{1, 4, 7},{2, 5, 8},{3, 6, 9},{1, 5, 9},{3, 5, 7}] # estas son todas las posibles combinaciones ganadoras que puede hacer un jugador

jugadorX = { # aqui se define al jugador X como un diccionario
    "name": 'Jugador X', # el atributo name será el nombre del jugador y se usara para indicar cuando le tocara jugar
    'indicador':'X', # el indicador sirve para mostrar en el tablero las casillas que marco este jugador
    "jugadas": set() # en este set se guardaran las jugadas que hizo el jugador
}
jugadorO = {
    "name": 'Jugador O',
    'indicador': 'O',
    "jugadas": set()
}

casillasOcupadas = []

def jugar():
    global ganador
    print('-----¿Cómo jugar?-----\nPara poner tu jugada en una casilla sigue este esquema:\n|1|2|3| \n|4|5|6| \n|7|8|9|')
    print("--------Comienza el juego--------") # primero se imprime por consola un string anunciando el inicio del juego
    renderTablero() # aqui se renderiza el tablero de juego
    jugadorTurno = jugadorX
    while ganador == False:
        HacerJugada(jugadorTurno)
        if jugadorTurno == jugadorX:
            jugadorTurno = jugadorO
        else:
            jugadorTurno = jugadorX


def renderTablero(): #Esta funcion es la encargada de renderizar el tablero de juego
    global tablero
    print("|{0}|{1}|{2}| \n|{3}|{4}|{5}| \n|{6}|{7}|{8}|".format(*tablero))
        


def pedirJugada(jugador):
    inputJugada = int(input('Ingrese la jugada del jugador ' + jugador['name'] + ': ')) -1
    if inputJugada in casillasOcupadas:
        print('Esa casilla ya está usada!!')
        return pedirJugada(jugador)
    else:
        if inputJugada > 9 or inputJugada < 0:
            print('---Debes elegir un número entre el 1 y el 9!!!')
            return pedirJugada(jugador)
        return inputJugada


def HacerJugada(jugador): # esta funcion se encarga de agregar una jugada a los movimientos de un jugador
    global ganador
    global tablero
    global casillasOcupadas
    print('Le toca al jugador ' + jugador['name']) # esta linea imprime por consola que le toca al jugador tal

    jugada = pedirJugada(jugador)
    casillasOcupadas.append(jugada)

    jugador['jugadas'].add(jugada+1)  # esta linea agrega al set jugadas del jugador, la jugada que hizo
    tablero[jugada] = jugador['indicador']  # esta linea actaliza al tablero con la jugada
    renderTablero() # aqui se renderiza el tablero nuevamente con la jugada ya actualizada

    for combinacionGanadora in combinacionesGanadoras:
        if len(combinacionGanadora & jugador['jugadas']) == 3:
          ganador = jugador
          print('---------------\n'+'Ganó el ' + ganador['name']+ '!!!\n' + '---------------')

jugar()