usuario = 'admin'
contrasena = '1234'

if usuario == 'admin':#si usuario es igual a admin
    if contrasena == '1234':#hace etsa pregunta
        print('Acceso concedido.')#si es correcta entonces permite el acceso
    else:#si no entonces
        print('Contraseña incorrecta.')#no deja hacer el login
else:#si de entrada el usuario es diferente de admin, entonces
    print('Usuario no reconocido.')#muestra este mensaje