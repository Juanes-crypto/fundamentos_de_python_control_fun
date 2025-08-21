fruta = input("Introduzca una fruta: ")#le pedimos al usuario que ingrese una furta

match fruta:#evaluamos el valor de fruta
    case "manzana":#en el caso de que se manzana, entonces
        print("La fruta es una manzana.")#muestra este mensaje
    case "naranja":# en el caso de que sea naranja entonces:
        print("La fruta es una naranja.")#muestra etse mensaje
    case "plátano":#en el caso de que sea platano
        print("La fruta es un plátano.")#muestra etse
    case _:#si no, entonces
        print("Fruta desconocida.")#imprime este mensaje