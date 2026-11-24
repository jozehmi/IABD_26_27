def procesar_lista(numeros):
    resultado = []
    
    for num in numeros:
        
        if num >= 0:
        
            repetido = False
            for r in resultado:
                if r == num:
                    repetido = True
                    break
            if repetido == False:
                resultado.append(num)
    
    n = len(resultado)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if resultado[j] > resultado[j + 1]:
                aux = resultado[j]
                resultado[j] = resultado[j + 1]
                resultado[j + 1] = aux
    
    return resultado

entrada = input("Introduce los números separados por comas o espacios: ")

entrada = entrada.replace(",", " ")

numeros = []
for lista in entrada.split():
    numeros.append(int(lista))

resultado = procesar_lista(numeros)
print("Lista procesada:", resultado)