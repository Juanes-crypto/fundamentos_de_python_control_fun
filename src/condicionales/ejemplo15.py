usuarios = [
    {"nombre": "Ana", "rol": "admin"},
    {"nombre": "Luis", "rol": "usuario"},
    {"nombre": "Marta", "rol": "moderador"}
]#se crea un array de objetos

for usuario in usuarios:#para usuario en usuarios se evalua el valor de
    match usuario:#usuario en el rol
        case {"rol": "admin"}:#si el rol es admin entonces
            print(f"{usuario['nombre']} tiene permisos de administrador.")#devuelve esta linea
        case {"rol": "moderador"}:#si el rol es moderador
            print(f"{usuario['nombre']} puede moderar contenidos.")#devuelve esta linea
        case {"rol": "usuario"}:#si el rol es usuario
            print(f"{usuario['nombre']} es un usuario regular.")#devuelve esta linea
        case _:#en el caso de que no exista o no encuentre un rol entonces
            print(f"Rol de {usuario['nombre']} desconocido.")#devuelve esta linea