def insercion_ordenar(lista):
    n = len(lista)
    i = 1
    
    while i < n:
        temp = lista[i]
        j = i - 1
        
        while j >= 0 and lista[j] > temp:
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = temp
        i += 1

# Ejemplo de uso
lista = [5, 3, 8, 1, 2, 7]
insercion_ordenar(lista)
print("Lista ordenada:", lista)

