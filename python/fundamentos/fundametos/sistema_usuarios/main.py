import getpass
from usuario import Usuario

def menu_principal():
    modelo_usuario = Usuario()
    while True:
        print("\n==============================")
        print("      SISTEMA DE USUARIOS     ")
        print("==============================")
        print("1. Iniciar sesión")
        print("2. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            usuario_input = input("Usuario: ").strip()
            password_input = getpass.getpass("Contraseña: ")
            
            usuario_logeado = modelo_usuario.validar_inicio_sesion(usuario_input, password_input)
            
            if usuario_logeado:
                if usuario_logeado.tipo == "ADMIN":
                    menu_administrador(usuario_logeado)
                elif usuario_logeado.tipo == "USER":
                    menu_usuario_comun(usuario_logeado)
            else:
                print("\n\x1b[31mUsuario o contraseña incorrectos.\x1b[0m")
        elif opcion == "2":
            print("¡Gracias por utilizar el sistema!")
            break

def menu_administrador(admin):
    modelo_usuario = Usuario()
    while True:
        print("\n==============================")
        print(f"Bienvenido Administrador:\n{admin.usuario.upper()}")
        print("==============================")
        print("1. Registrar usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario")
        print("4. Modificar usuario")
        print("5. Eliminar usuario")
        print("6. Cerrar sesión")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            print("\n--- Registrar Usuario ---")
            u = input("Nuevo Usuario: ").strip()
            p = input("Contraseña: ").strip()
            t = input("Tipo (ADMIN o USER): ").strip().upper()
            if t in ["ADMIN", "USER"]:
                if modelo_usuario.crear_usuario(u, p, t):
                    print("\x1b[32mUsuario registrado con éxito.\x1b[0m")
            else:
                print("\x1b[31mTipo de usuario no válido.\x1b[0m")
                
        elif opcion == "2":
            print("\n--- Listado de Usuarios ---")
            usuarios = modelo_usuario.obtener_listado()
            print(f"{'ID':<6} {'Usuario':<15} {'Tipo':<10}")
            print("-" * 31)
            for row in usuarios:
                print(f"{row['id']:<6} {row['usuario']:<15} {row['tipo']:<10}")
            print(f"\nTotal usuarios: {modelo_usuario.contar_total_usuarios()}")
            
        elif opcion == "3":
            print("\n--- Buscar Usuario ---")
            id_busqueda = input("Ingrese el ID del usuario: ").strip()
            res = modelo_usuario.buscar_por_id(id_busqueda)
            if res:
                print(f"\nID: {res['id']}\nUsuario: {res['usuario']}\nTipo: {res['tipo']}")
                print(f"Creado: {res['fecha_creacion']}\nModificado: {res['ultima_modificacion']}")
            else:
                print("\x1b[31mUsuario no encontrado.\x1b[0m")
                
        elif opcion == "4":
            print("\n--- Modificar Usuario ---")
            id_mod = input("Ingrese el ID a modificar: ").strip()
            res = modelo_usuario.buscar_por_id(id_mod)
            if res:
                u = input(f"Nuevo usuario [{res['usuario']}]: ").strip() or res['usuario']
                p = input(f"Nueva contraseña [{res['password']}]: ").strip() or res['password']
                t = input(f"Nuevo tipo [{res['tipo']}]: ").strip().upper() or res['tipo']
                if t in ["ADMIN", "USER"]:
                    modelo_usuario.modificar_usuario(id_mod, u, p, t)
                    print("\x1b[32mModificado con éxito.\x1b[0m")
            else:
                print("\x1b[31mUsuario no encontrado.\x1b[0m")
                
        elif opcion == "5":
            print("\n--- Eliminar Usuario ---")
            id_del = input("Ingrese el ID a eliminar: ").strip()
            res = modelo_usuario.buscar_por_id(id_del)
            if res:
                confirmar = input(f"¿Eliminar a {res['usuario']}? (s/n): ").strip().lower()
                if confirmar == 's':
                    modelo_usuario.eliminar_usuario(id_del)
                    print("\x1b[32mEliminado correctamente.\x1b[0m")
            else:
                print("\x1b[31mUsuario no encontrado.\x1b[0m")
                
        elif opcion == "6":
            break

def menu_usuario_comun(user):
    while True:
        print("\n==============================")
        print(f"Bienvenido\n\n{user.usuario.capitalize()}")
        print(f"\nTipo de usuario:\n{user.tipo}")
        print("==============================")
        print("1. Cerrar sesión")
        
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            break

if __name__ == "__main__":
    menu_principal()