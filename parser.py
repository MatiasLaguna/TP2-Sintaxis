import lexer
pila = ["EOF", "Program"]
indice = 0
tabla = {"Program": {"clp": [], "si": ["Estructura", "Program"], "id": ["Estructura", "Program"], "mientras": ["Estructura", "Program"], "mostrar": ["Estructura", "Program"], "aceptar": ["Estructura", "Program"], "EOF": []},
         "Termino2": {"*": ["*", "Factor", "Termino2"], "+": [], "entonces": [], ")": [], "EOF": [], "mientras": [], "mostrar": [], "aceptar": [], "si": [], "id": [], "clp": []},
         "Estructura": {"id": ["id", "eq", "Expresion"], "si": ["si", "Expresion", "entonces", "op", "Program", "clp", "sino", "op", "Program", "clp"], "mostrar": ["mostrar", "Expresion"], "aceptar": ["aceptar", "id"], "mientras": ["mientras", "id", "esMenorQue", "Valor", "hacer", "op", "Program", "clp"]},
         "Expresion": {"id": ["Termino", "Expresion2"], "num": ["Termino", "Expresion2"], "(": ["Termino", "Expresion2"]},
         "Valor": {"id": ["id"], "num": ["num"]},
         "Expresion2": {"+": ["+", "Termino", "Expresion2"], "entonces": [], ")": [], "EOF": [], "mientras": [], "mostrar": [], "aceptar": [], "si": [], "id": [], "clp": []},
         "Termino": {"id": ["Factor", "Termino2"], "num": ["Factor", "Termino2"], "(": ["Factor", "Termino2"], "EOF": []},
         "Factor": {"id": ["Valor"], "num": ["Valor"], "(": ["(", "Expresion", ")"]}
         }
VT = ["id", "num", "(", ")", "+", "*", "si", "entonces", "sino", "mientras",
      "esMenorQue", "hacer", "mostrar", "aceptar", "op", "clp", "eq", "EOF"]

VN = ["Program", "Termino2", "Estructura", "Expresion",
      "Valor", "Expresion2", "Termino", "Factor"]


def parser(lista_tokens):
    indice = 0
    producciones = []
    while pila[-1] != "EOF" or lista_tokens[indice][0] != "EOF":
        if pila[-1] in VT:
            if pila[-1] == lista_tokens[indice][0]:
                pila.pop()
                indice += 1
            else:
                print("Cadena no aceptada")
                return False
        elif pila[-1] in VN:
            if lista_tokens[indice][0] in tabla[pila[-1]]:
                last = pila.pop()
                pila.extend((tabla[last][lista_tokens[indice][0]])[::-1])
                parteDerecha = tabla[last][lista_tokens[indice][0]]
                producciones.append(
                    last + " -> " + " ".join(parteDerecha if parteDerecha != [] else ["lambda"]))
            else:
                print("Cadena no aceptada")
                return False
    print("Cadena aceptada")
    print("Producciones: "+", ".join(producciones))
    return True


# parser(lexer.lexer("mostrar si#"))
# parser(lexer.lexer("mientras id esMenorQue a hacer op clp#"))
parser(lexer.lexer(
    "si (aux+bux)*cont entonces op mostrar aux clp sino op aceptar bux clp#"))
# parser(lexer.lexer("id eq (num)* id#"))
