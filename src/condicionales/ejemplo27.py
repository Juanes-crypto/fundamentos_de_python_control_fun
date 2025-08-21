a = 5
b = 10
c = 15

if a > b:#si a es mayor que b entonces
    if a > c:#entra en esta evaluacion, si es positiva entonces
        print('a es el mayor.')#muestra este mensaje
    else:#si la segundo evualuacion es negativa entonces
        if c > b:#hace esta evaluacion
            print('c es el mayor.')#si la cumple muestra esta liena
        else:#si no la cumple muestra esta otra
            print('b es el mayor.')
else:#si desde el inicio a no es mayor que b entonces
    if b > c:#entonces muestra esto
        print('b es el mayor.')
    else:#si no entonces muestra esto de abajo
        print('c es el mayor.')