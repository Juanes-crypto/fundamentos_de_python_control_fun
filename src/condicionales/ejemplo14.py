edad = 20#iniciamos con la variable edad en 20

match edad:#se evalua el valor de edad
    case edad if edad < 18:#en el caso de que edad sea mayor a 18
        print("Eres menor de edad.")#entonces se ejecuta esto
    case edad if edad >= 18 and edad < 65:#si edad este en el rango de 18 y 65
        print("Eres adulto.")#entonces se ejecuta esto
    case edad if edad >= 65:#si edad es mayor a 65
        print("Eres adulto mayor.")#entonces se ejecuta esto