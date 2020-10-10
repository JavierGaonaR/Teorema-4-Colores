# Faltaron estados :(
estados = [
    ['Aguascalientes', ['Zacatecas', 'San Luis Potosi', 'Jalisco']],
    ['Baja California Norte', ['Baja California Sur', 'Sonora']],
    ['Baja California Sur', ['Baja California Norte']],
    ['Sonora', ['Baja California Norte', 'Chihuahua', 'Sinaloa']],
    ['Chihuahua', ['Sonora', 'Sinaloa', 'Durango', 'Coahuila']],
    ['Sinaloa', ['Sonora', 'Chihuahua', 'Durango']],
    ['Durango', ['Chihuahua', 'Sinaloa', 'Coahuila', 'Zacatecas']],
    ['Coahuila', ['Chihuahua', 'Durango', 'Zacatecas', 'Nuevo Leon']],
    ['Nuevo Leon', ['Coahuila', 'Tamaulipas', 'San Luis Potosi']],
    ['Tamaulipas', ['Nuevo Leon', 'San Luis Potosi', 'Veracruz']],
    ['Jalisco', ['Michoacan', 'Aguascalientes', 'Zacatecas']],
    ['San Luis Potosi', ['Nuevo Leon', 'Zacatecas','Veracruz', 'Tamaulipas']],
    ['Zacatecas', ['Durango', 'Coahuila', 'San Luis Potosi', 'Aguascalientes', 'Jalisco']],
    ['Michoacan', ['Jalisco', 'Guerrero']],
    ['Guerrero', ['Michoacan', 'Oaxaca']],
    ['Veracruz', ['Tamaulipas', 'San Luis Potosi', 'Chiapas', 'Oaxaca']],
    ['Oaxaca', ['Guerrero', 'Chiapas', 'Veracruz']],
    ['Chiapas', ['Oaxaca', 'Veracruz', 'Campeche']],
    ['Campeche', ['Chiapas', 'Yucatan', 'Quintana Roo']],
    ['Yucatan', ['Quintana Roo', 'Campeche']],
    ['Quintana Roo', ['Campeche', 'Quintana Roo']]
]


def buscar(lista, nombre):
    for estado in lista:
        if estado[0] == nombre:
            return estado
    return 'Null'

def buscarColorPadre(lista, nombre):
    for elemento in lista:
        if elemento[0] == nombre:
            return elemento

def esExplorado(lista, exploreded):
    for elemento in lista:
        if elemento[0] == exploreded:
            return True
    return False

def consultarExplorado(lista, nombre):
    for elemento in lista:
        if elemento[0] == nombre:
            return elemento
    return 'Null'

def bfs(inicio):
    queue = list()
    queue.append(buscar(estados, inicio))

    explored = list()
    explored.append([inicio, colores[0]])

    while len(queue) > 0:
        v = queue.pop()

        if len(estados) == len(explored):
            for exp in explored:
                print(exp)
            return None
        
        for i, hijo in enumerate(v[1]):
            n = len(v[1]) - 1
            indexColor = -1
            coloresDisponibles = []

            # Se buscan los colores de los nodos adyacentes
            nodoIzquierdo = 'Null'
            nodoDerecho = 'Null'
            nodoPadre = buscarColorPadre(explored, v[0])

            # Indices de los nodos adyacentes
            j = -1
            h = -1

            # Seleccion de color
            if n > 1:
                if i == 0:
                    j = 1
                    nodoDerecho = consultarExplorado(explored, v[1][j])
                elif i == n: 
                    h = n - 1
                    nodoIzquierdo = consultarExplorado(explored, v[1][h])
                elif i > 0 and i < n:
                    j = i - 1
                    h = i + 1
                    nodoIzquierdo = consultarExplorado(explored, v[1][j])
                    nodoDerecho = consultarExplorado(explored, v[1][h])

            if not nodoIzquierdo == 'Null' and nodoDerecho == 'Null':
                coloresDisponibles = []
                for color in colores:
                    if not (nodoPadre[1] == color or nodoIzquierdo[1] == color):
                        coloresDisponibles.append(color)
                        continue
                indexColor = colores.index(coloresDisponibles[0])
            elif not nodoDerecho == 'Null' and nodoIzquierdo == 'Null':
                coloresDisponibles = []
                for color in colores:
                    if not (nodoPadre[1] == color or nodoDerecho[1] == color):
                        coloresDisponibles.append(color)
                        continue
                indexColor = colores.index(coloresDisponibles[0])
            elif not (nodoDerecho == 'Null' and nodoIzquierdo == 'Null'):
                coloresDisponibles = []
                for color in colores:
                    if not (nodoPadre[1] == color or nodoIzquierdo[1] == color or nodoDerecho[1] == color):
                        coloresDisponibles.append(color)
                        continue
                indexColor = colores.index(coloresDisponibles[0])
            else:
                coloresDisponibles = []
                for color in colores:
                    if not nodoPadre[1] == color:
                        coloresDisponibles.append(color)
                        continue
                indexColor = colores.index(coloresDisponibles[0])

            nodoActual = buscar(estados, hijo)
            nodosVecinos = []
            for nodo in nodoActual[1]:
                tmp = buscar(explored, nodo)
                if tmp != 'Null': 
                    nodosVecinos.append(tmp)
            for nodo in nodosVecinos:
                if nodo[1] in coloresDisponibles:
                    del coloresDisponibles[coloresDisponibles.index(nodo[1])]
                    indexColor = colores.index(coloresDisponibles[0])
            

            if not esExplorado(explored, hijo):
                explored.append([hijo, colores[indexColor]])
                queue.append(buscar(estados, hijo))

    print(explored)


color_default = 'Blanco'
colores = ['Naranja', 'Morado', 'Amarillo', 'Azul', 'Verde']

bfs('Nuevo Leon')