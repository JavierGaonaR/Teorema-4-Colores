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


def buscar(nombre):
    for estado in estados:
        if estado[0] == nombre:
            return estado

def buscarColorPadre(lista, nombre):
    for elemento in lista:
        if elemento[0] == nombre:
            return elemento[1]

def esExplorado(lista, exploreded):
    for elemento in lista:
        if elemento[0] == exploreded:
            return True
    return False

def bfs(inicio):
    queue = list()
    queue.append(buscar(inicio))

    explored = list()
    explored.append([inicio, colores[0]])

    while len(queue) > 0:
        v = queue.pop()

        if len(estados) == len(explored):
            for exp in explored:
                print(exp)
            return None
        
        for i, hijo in enumerate(v[1]):
            n = len(v[1])

            # Se buscan los colores de los nodos adyacentes
            nodoIzquierdo = -1
            nodoDerecho = -1
            nodoPadre = buscarColorPadre(explored, v[0])

            if i == 0 :
                j = i + 1

            elif i == n:
                j = n - 1
            
            else:
                None

            # Edit: Aun no selecciona el color distinto a los demas, la parte de arriba lo haria
            if not esExplorado(explored, hijo):
                explored.append([hijo, colores[i]])
                queue.append(buscar(hijo))

    print(explored)


color_default = 'Blanco'
colores = ['Naranja', 'Morado', 'Amarillo', 'Azul', 'Verde']

bfs('Nuevo Leon')