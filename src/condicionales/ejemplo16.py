numeros = [1, 2, 3, 4]#se crea un array de numeros

match numeros:#se evlua el valor de numeros
    case []:#en el caso de que el array este vacio
        print("La lista está vacía.")#muestra esto
    case [uno]:#en el caso de que el tamaño del array sea uno
        print(f"Un solo elemento: {uno}.")#muestra esto
    case [uno, dos]:#en el caso de que tenga dos elementos
        print(f"Dos elementos: {uno} y {dos}.")#muestra esto
    case [uno, *resto]:#y si tiene mas de dos elementos, etncones con *resto muestra el resto de elementos
        print(f"Primer elemento: {uno}, resto de la lista: {resto}.")#muestra esto