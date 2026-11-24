import string

def normalizar(texto):

    texto = texto.lower()

    for signo in string.punctuation:
        texto = texto.replace(signo, " ")
    
    texto = texto.replace("¿", " ")
    texto = texto.replace("¡", " ")

    texto = texto.replace("á", "a").replace("é", "e").replace("í", "i")
    texto = texto.replace("ó", "o").replace("ú", "u").replace("ü", "u")
    texto = texto.replace("ñ", "n")

    return texto

def frecuencia_palabras(lista_palabras, ruta_fichero):
    
    frecuencias = {}
    for palabra in lista_palabras:
        palabra_limpia = normalizar(palabra).strip()
        if palabra_limpia != "":   # evitar palabras vacías
            frecuencias[palabra_limpia] = 0

    with open(ruta_fichero, "r", encoding="utf-8") as fichero:
        contenido = normalizar(fichero.read())

    for palabra in contenido.split():
        if palabra in frecuencias:
            frecuencias[palabra] = frecuencias[palabra] + 1

    return frecuencias

if __name__ == "__main__":
    
    ruta = input("Introduce la ruta del fichero: ").strip('"').strip("'")
    entrada = input("Introduce las palabras separadas por comas: ")

    lista_palabras = entrada.replace(",", " ").split()

    resultado = frecuencia_palabras(lista_palabras, ruta)

    print("\nFrecuencia de palabras (ordenadas alfabéticamente):")
    for palabra in sorted(resultado):
        print(f"  {palabra}: {resultado[palabra]}")