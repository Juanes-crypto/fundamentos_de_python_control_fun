edad = 16#variable int
permiso_padres = True#vareable boleana

if edad >= 18:#si edad es mayor o igual a 18 entonces
    print('Puedes obtener la licencia de conducir.')#muestra etse mensaje
else:#si no entonces
    if edad >= 16:#hace esta pregunta
        if permiso_padres:#si la pregunta anterior es positiva entoncces pregunta esto
            print('Puedes obtener la licencia con permiso de tus padres.')#si tambien es positiva entonces imprime esto
        else:#si la de los padres no es positiva entonces
            print('Necesitas el permiso de tus padres para obtener la licencia.')#imprime esto
    else:#si es menor de edad, directamente no dice esto
        print('Eres demasiado joven para conducir.')