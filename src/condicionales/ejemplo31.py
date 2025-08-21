numeros = [1, 2, 3, 4, 5]#array de numeros
paridad = ["par" if n % 2 == 0 else "impar" for n in numeros]#debvuelve par si el numero con modulo dos da cero y devuelve impar si da 1
#con el for in va iterando y se va haciendo esas dos pregutnas por cada iteracion
print(paridad)  # Salida: ['impar', 'par', 'impar', 'par', 'impar']