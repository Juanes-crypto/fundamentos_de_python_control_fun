saldo = 300# se declaran dos variables 
retiro = 500
if saldo >= retiro:# si saldoo es mayor o igual a retiro entonces
    saldo -= retiro# se le resta el valor de retiro a saldo y el valor de esa resta se asigna al saldo
    print("Retiro exitoso.")# se imrpime este mensaje
    print(f"Nuevo saldo: {saldo}")# en este print, con la ayuda de "f" podemos anexar variables simplemente usando las llaves
else:# si no entonces:
    print("Fondos insuficientes.")# este mensaje se imprime
    print(f"Saldo actual: {saldo}")# y este menssaje se imprime mostrando el saldo