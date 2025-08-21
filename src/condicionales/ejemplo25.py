edad = 16
permiso_padres = True

if edad >= 18:
    print('Puedes obtener la licencia de conducir.')
elif edad >= 16 and permiso_padres:
    print('Puedes obtener la licencia con permiso de tus padres.')
elif edad >= 16 and not permiso_padres:
    print('Necesitas el permiso de tus padres para obtener la licencia.')
else:
    print('Eres demasiado joven para conducir.')

#si la edad es mayor o igual a 18 entonces lanza el mensaje de la linea 5, si no entra a la siguiente pregunta
#si la edad es mayor o igual a 16 entonces lanza el mensaje de la linea 7
#si no entonces evalua la siguiente pregunta: si edad es mayor o igual a 16 y NO tiene permiso entonces
#lanza el mensaje de la linea 9
#si no entonces, es menor de edad y es demaciado joven
 