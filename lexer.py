ESTADO_TRAMPA = "TRAMPA"

ESTADO_FINAL = "ACEPTADO"

ESTADO_NO_FINAL = "NO ACEPTADO"


def condicion_cadena(estado_actual1, estados_finaless):

    if estado_actual1 == -1:
        return ESTADO_TRAMPA
    if estado_actual1 in estados_finaless:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL


def automata_eq(cadena):

    estado_actual = 0
    estados_finales = [2]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "e":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "q":
            estado_actual = 2
        else:
            estado_actual = -1
            break

    return condicion_cadena(estado_actual, estados_finales)


def automata_id(cadena):

    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
              "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    estado_actual = 0
    estados_finales = [1]
    for caracter in cadena:
        if estado_actual == 0 and caracter in letras:
            estado_actual = 1
        elif estado_actual == 1 and (caracter in letras or caracter in numeros):
            estado_actual = 1
        else:
            estado_actual = -1
    return condicion_cadena(estado_actual, estados_finales)


def automata_num(cadena):

    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    estado_actual = 0
    estados_finales = [1]
    for caracter in cadena:
        if estado_actual == 0 and (caracter in numeros):
            estado_actual = 1
        elif estado_actual == 1 and (caracter in numeros):
            estado_actual = 1
        else:
            estado_actual = -1
            break
    return condicion_cadena(estado_actual, estados_finales)


def automata_op(cadena):

    estado_actual = 0
    estados_finales = [2]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "o":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "p":
            estado_actual = 2
        else:
            estado_actual = -1
            break

    return condicion_cadena(estado_actual, estados_finales)


def automata_clp(cadena):

    estado_actual = 0
    estados_finales = [3]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "c":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "l":
            estado_actual = 2
        elif estado_actual == 2 and caracter == "p":
            estado_actual = 3
        else:
            estado_actual = -1
            break

    return condicion_cadena(estado_actual, estados_finales)


def automata_si(cadena):

    estado_actual = 0
    estados_finales = [2]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "s":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "i":
            estado_actual = 2
        else:
            estado_actual = -1
            break

    return condicion_cadena(estado_actual, estados_finales)


def automata_entonces(cadena):

    estado_actual = 0
    estados_finales = [8]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "e":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "n":
            estado_actual = 2
        elif estado_actual == 2 and caracter == "t":
            estado_actual = 3
        elif estado_actual == 3 and caracter == "o":
            estado_actual = 4
        elif estado_actual == 4 and caracter == "n":
            estado_actual = 5
        elif estado_actual == 5 and caracter == "c":
            estado_actual = 6
        elif estado_actual == 6 and caracter == "e":
            estado_actual = 7
        elif estado_actual == 7 and caracter == "s":
            estado_actual = 8

        else:
            estado_actual = -1
            break

    return condicion_cadena(estado_actual, estados_finales)


def automata_sino(cadena):

    estado_actual = 0
    estados_finales = [4]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "s":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "i":
            estado_actual = 2
        elif estado_actual == 2 and caracter == "n":
            estado_actual = 3
        elif estado_actual == 3 and caracter == "o":
            estado_actual = 4

        else:
            estado_actual = -1
            break

    return condicion_cadena(estado_actual, estados_finales)


def automata_mostrar(cadena):

    estado_actual = 0
    estados_finales = [7]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "m":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "o":
            estado_actual = 2
        elif estado_actual == 2 and caracter == "s":
            estado_actual = 3
        elif estado_actual == 3 and caracter == "t":
            estado_actual = 4
        elif estado_actual == 4 and caracter == "r":
            estado_actual = 5
        elif estado_actual == 5 and caracter == "a":
            estado_actual = 6
        elif estado_actual == 6 and caracter == "r":
            estado_actual = 7
        else:
            estado_actual = -1
            break

    return condicion_cadena(estado_actual, estados_finales)


def automata_aceptar(cadena):

    estado_actual = 0
    estados_finales = [7]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "a":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "c":
            estado_actual = 2
        elif estado_actual == 2 and caracter == "e":
            estado_actual = 3
        elif estado_actual == 3 and caracter == "p":
            estado_actual = 4
        elif estado_actual == 4 and caracter == "t":
            estado_actual = 5
        elif estado_actual == 5 and caracter == "a":
            estado_actual = 6
        elif estado_actual == 6 and caracter == "r":
            estado_actual = 7
        else:
            estado_actual = -1
            break

    return condicion_cadena(estado_actual, estados_finales)


def automata_mientras(cadena):

    estado_actual = 0
    estados_finales = [8]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "m":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "i":
            estado_actual = 2
        elif estado_actual == 2 and caracter == "e":
            estado_actual = 3
        elif estado_actual == 3 and caracter == "n":
            estado_actual = 4
        elif estado_actual == 4 and caracter == "t":
            estado_actual = 5
        elif estado_actual == 5 and caracter == "r":
            estado_actual = 6
        elif estado_actual == 6 and caracter == "a":
            estado_actual = 7
        elif estado_actual == 7 and caracter == "s":
            estado_actual = 8
        else:
            estado_actual = -1
            break

    return condicion_cadena(estado_actual, estados_finales)


def automata_esMenorQue(cadena):

    estado_actual = 0
    estados_finales = [10]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "e":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "s":
            estado_actual = 2
        elif estado_actual == 2 and caracter == "M":
            estado_actual = 3
        elif estado_actual == 3 and caracter == "e":
            estado_actual = 4
        elif estado_actual == 4 and caracter == "n":
            estado_actual = 5
        elif estado_actual == 5 and caracter == "o":
            estado_actual = 6
        elif estado_actual == 6 and caracter == "r":
            estado_actual = 7
        elif estado_actual == 7 and caracter == "Q":
            estado_actual = 8
        elif estado_actual == 8 and caracter == "u":
            estado_actual = 9
        elif estado_actual == 9 and caracter == "e":
            estado_actual = 10
        else:
            estado_actual = -1
            break

    return condicion_cadena(estado_actual, estados_finales)


def automata_hacer(cadena):

    estado_actual = 0
    estados_finales = [5]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "h":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "a":
            estado_actual = 2
        elif estado_actual == 2 and caracter == "c":
            estado_actual = 3
        elif estado_actual == 3 and caracter == "e":
            estado_actual = 4
        elif estado_actual == 4 and caracter == "r":
            estado_actual = 5
        else:
            estado_actual = -1
            break

    return condicion_cadena(estado_actual, estados_finales)


def automata_abrir_parentesis(cadena):
    simbolos = ["("]

    estado_actual = 0
    estados_finales = [1]

    for caracter in cadena:
        if estado_actual == 0 and caracter in simbolos:
            estado_actual = 1
        else:
            estado_actual = -1
            break

    return condicion_cadena(estado_actual, estados_finales)


def automata_cerrar_parentesis(cadena):
    simbolos = [")"]

    estado_actual = 0
    estados_finales = [1]

    for caracter in cadena:
        if estado_actual == 0 and caracter in simbolos:
            estado_actual = 1
        else:
            estado_actual = - 1
            break

    return condicion_cadena(estado_actual, estados_finales)


def automata_suma(cadena):
    simbolos = ["+"]

    estado_actual = 0
    estados_finales = [1]

    for caracter in cadena:
        if estado_actual == 0 and caracter in simbolos:
            estado_actual = 1
        else:
            estado_actual = - 1
            break

    return condicion_cadena(estado_actual, estados_finales)


def automata_multiplicacion(cadena):
    simbolos = ["*"]

    estado_actual = 0
    estados_finales = [1]

    for caracter in cadena:
        if estado_actual == 0 and caracter in simbolos:
            estado_actual = 1
        else:
            estado_actual = - 1
            break

    return condicion_cadena(estado_actual, estados_finales)


def automata_EOF(cadena):
    simbolos = ["#"]

    estado_actual = 0
    estados_finales = [1]

    for caracter in cadena:
        if estado_actual == 0 and caracter in simbolos:
            estado_actual = 1
        else:
            estado_actual = - 1
            break

    return condicion_cadena(estado_actual, estados_finales)

# DEFINIMOS CADA VT
    # VT = {eq, id, num, *, +, op, clp, si, entonces, sino, mostrar, aceptar, mientras, esMenorQue, hacer, (, )}


TOKENS = [("sino", automata_sino), ("si", automata_si), ("entonces", automata_entonces), ("mostrar", automata_mostrar), ("aceptar", automata_aceptar), ("num", automata_num), ("mientras", automata_mientras), ("esMenorQue", automata_esMenorQue),
          ("hacer", automata_hacer), ("*", automata_multiplicacion),  ("+", automata_suma), ("eq", automata_eq), ("(", automata_abrir_parentesis), (")", automata_cerrar_parentesis), ("op", automata_op), ("clp", automata_clp), ("id", automata_id), ("EOF", automata_EOF)]

def lexer(codigofuente):
    error = 0
    inicio_lex = 0
    tokens = []
    posicion_actual = 0
    while posicion_actual < len(codigofuente):
        while codigofuente[posicion_actual].isspace():
            posicion_actual += 1
        inicio_lex = posicion_actual
        posibles_tokens = []
        posibles_tokens_aux = []
        lexema = ""
        todos_en_estado_trampa = False

        while not todos_en_estado_trampa and posicion_actual < len(codigofuente)+1:
            todos_en_estado_trampa = True
            lexema = codigofuente[inicio_lex: posicion_actual+1]
            posibles_tokens = posibles_tokens_aux
            posibles_tokens_aux = []
            for (tipoToken, afd) in TOKENS:
                simulo_afd = afd(lexema)
                if simulo_afd == ESTADO_FINAL:
                    posibles_tokens_aux.append(tipoToken)
                    todos_en_estado_trampa = False
                elif simulo_afd == ESTADO_NO_FINAL:
                    todos_en_estado_trampa = False
            posicion_actual += 1

        if len(posibles_tokens) == 0:
            print("ERROR : TOKEN DESCONOCIDO " + lexema)
            error = 1
        else:
            posicion_actual -= 1
            token = (posibles_tokens[0],
                     codigofuente[inicio_lex:posicion_actual])
            tokens.append(token)

    return tokens if error == 0 else ""


# print(lexer("si (a esMenorQue b) entonces op mostrar * (a) clp sino op mostrar (b) clp"))
# print(lexer("sino 12 si aux (mostrar 345cont)"))
# print(lexer("si 10 * 10 entonces aceptar (mostrar 345cont)"))
