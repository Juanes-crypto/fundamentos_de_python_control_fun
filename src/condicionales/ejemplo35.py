condiciones = [True, True, False, True]#array de booleanos

if all(condiciones):#esto se detendra al encontrar un valor falso
    print("Todas las condiciones son verdaderas.")#muestra esto hasta que encuentre un false
else:
    print("Al menos una condición es falsa.")#esto pasa cuando encuentra el false