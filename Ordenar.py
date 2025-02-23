def ordenar_por_insercion(lista):
    tamaño = len(lista)
    
    for i in range(1, tamaño):
        valor_actual = lista[i]
        j = i - 1
        
        while j >= 0 and lista[j] > valor_actual:
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = valor_actual

# Ejemplo de uso
datos = [5, 3, 8, 1, 2, 7]
ordenar_por_insercion(datos)
print("Lista ordenada:", datos)
