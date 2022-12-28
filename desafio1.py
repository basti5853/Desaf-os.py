def es_palindromo(frase):
    frase = frase.lower() # pasa todo a minuscula
    frase = frase.replace( ' ', '') #reemplaza el prier elemento del parentesis por el 2
    longitud = len(frase) # largo/longitud de la frase

    if longitud % 2 == 0: # % te saca el resto de la division
    # caso 1: NUMERO PAR
        izquierda = frase[:longitud // 2] # //: funcion parte entera, o piso. (te saca el entero mas bajo de la divison)
        derecha = frase[longitud// 2:]
        print(izquierda)
        print(derecha)
    else: #
        # caso2: NUMERO IMPAR
        izquierda = frase[:longitud // 2]
        derecha = frase[longitud // 2 + 1:] # no considera el elemtno del medio.
    
    return izquierda == derecha[::-1 ]