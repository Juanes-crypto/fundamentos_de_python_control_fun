punto = (0, 0)# se inicia un patron

match punto:#evaluamos el valor de ese patron
    case (0, 0):#en el caso de que sea 0.0
        print("El punto está en el origen.")#se ejecuta esta linea de codigo
    case (0, y):#en el caso de que sea0 y un valor y
        print(f"El punto está en el eje Y en y={y}.")#se ejecuta esta linea de codigo
    case (x, 0):#en el caso de que sea un valor x y cero
        print(f"El punto está en el eje X en x={x}.")#se ejecuta esta linea de codigo
    case (x, y):#en el caso de que sea un valor x y y entonces
        print(f"El punto está en coordenadas x={x}, y={y}.")#se ejecuta esta linea de codigo