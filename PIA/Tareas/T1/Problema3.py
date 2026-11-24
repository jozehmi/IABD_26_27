def operaciones_conjuntos(lista1, lista2):
    
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    #Dicionario de resultados usando operaciones de conjuntos
    resultado = {
        "interseccion": conjunto1 & conjunto2,          # elementos comunes
        "union": conjunto1 | conjunto2,                 # todos sin duplicados
        "diferencia_simetrica": conjunto1 ^ conjunto2   # en uno u otro, pero no en ambos
    }

    return resultado

if __name__ == "__main__":

    entrada1 = input("Introduce los números de la primera lista (separados por comas): ")
    entrada2 = input("Introduce los números de la segunda lista (separados por comas): ")

    lista1 = []
    for trozo in entrada1.replace(",", " ").split():
        lista1.append(int(trozo))

    lista2 = []
    for trozo in entrada2.replace(",", " ").split():
        lista2.append(int(trozo))

    resultado = operaciones_conjuntos(lista1, lista2)

    print("\n--- Resultados ---")
    print("Intersección (elementos comunes):")
    print("  ", sorted(resultado["interseccion"]))

    print("Unión (todos sin duplicados):")
    print("  ", sorted(resultado["union"]))

    print("Diferencia simétrica (en uno u otro, pero no en ambos):")
    print("  ", sorted(resultado["diferencia_simetrica"]))