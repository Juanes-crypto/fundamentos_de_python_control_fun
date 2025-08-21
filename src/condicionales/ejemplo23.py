edad = 30#variable de tipo int
estado_civil = 'soltero'#variable de tipo string

if edad >= 18:# si edad es mayor o igual a 18
    if estado_civil == 'casado':#si cumple la condiciond e arriba, evalua esta pregunta
        print('Eres un adulto casado.')# si cumple con ambas entonces imprime esto
    else:#si no entonces
        print('Eres un adulto soltero.')#imprime esto si no cumple la segunda condicion
else:
    print('Eres menor de edad.')# si de entrada no es mayor de edad, entonces muestra este mensaje