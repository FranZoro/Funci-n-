def ganador(clientes, puntos):
    ganador = ""
    indice_mayor = ""
    punto_mayor = 0
    for i in range(len(puntos)):
        if puntos[i] > punto_mayor:
            punto_mayor = puntos[i]
            indice_mayor = i
    ganador = clientes[indice_mayor]
    return ganador
clientes = ["Luis", "Julieta", "Hernan", "Lara"]
puntos = [1200, 45, 1240, 5000]
print(ganador(clientes, puntos))


