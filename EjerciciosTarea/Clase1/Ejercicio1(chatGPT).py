def probabilidad_numero_par():
    # Número de resultados favorables (números pares)
    resultados_favorables = 3
    
    # Número total de resultados posibles
    resultados_posibles = 6
    
    # Cálculo de la probabilidad
    probabilidad = resultados_favorables / resultados_posibles
    
    return probabilidad

# Llamada a la función para obtener la probabilidad
probabilidad = probabilidad_numero_par()

print("La probabilidad de obtener un número par en un lanzamiento de un dado estándar es:", probabilidad)
