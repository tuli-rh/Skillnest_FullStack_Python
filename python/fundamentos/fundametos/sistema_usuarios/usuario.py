from conexion import Conexion
import pymysql

class Usuario:
    def __init__(self, id=None, usuario=None, password=None, tipo=None):
        self.id = id
        self.usuario = usuario
        self.password = password
        self.tipo = tipo

    def validar_inicio_sesion(self, txt_usuario, txt_password):
        db = Conexion()
        con = db.conectar()
        if not con: return None
        try:
            with con.cursor() as cursor:
                sql = """
                    SELECT u.id, u.usuario, u.password, t.nombre AS tipo 
                    FROM usuarios u
                    INNER JOIN tipos_usuario t ON u.tipo_usuario_id = t.id
                    WHERE u.usuario = %s AND u.password = %s
                """
                cursor.execute(sql, (txt_usuario, txt_password))
                res = cursor.fetchone()
                if res:
                    return Usuario(res['id'], res['usuario'], res['password'], res['tipo'])
                return None
        finally:
            db.cerrar()

    def existe_usuario(self, txt_usuario):
        db = Conexion()
        con = db.conectar()
        try:
            with con.cursor() as cursor:
                cursor.execute("SELECT id FROM usuarios WHERE usuario = %s", (txt_usuario,))
                return cursor.fetchone() is not None
        finally:
            db.cerrar()

    def crear_usuario(self, txt_usuario, txt_password, txt_tipo):
        if self.existe_usuario(txt_usuario):
            print("\x1b[31mError: El usuario ya existe.\x1b[0m")
            return False
        db = Conexion()
        con = db.conectar()
        try:
            with con.cursor() as cursor:
                cursor.execute("SELECT id FROM tipos_usuario WHERE nombre = %s", (txt_tipo,))
                rol = cursor.fetchone()
                if not rol: return False
                
                sql = "INSERT INTO usuarios (usuario, password, tipo_usuario_id) VALUES (%s, %s, %s)"
                cursor.execute(sql, (txt_usuario, txt_password, rol['id']))
                con.commit()
                return True
        finally:
            db.cerrar()

    def obtener_listado(self):
        db = Conexion()
        con = db.conectar()
        try:
            with con.cursor() as cursor:
                sql = """
                    SELECT u.id, u.usuario, t.nombre AS tipo 
                    FROM usuarios u
                    INNER JOIN tipos_usuario t ON u.tipo_usuario_id = t.id
                    ORDER BY u.id ASC
                """
                cursor.execute(sql)
                return cursor.fetchall()
        finally:
            db.cerrar()

    def buscar_por_id(self, id_usuario):
        db = Conexion()
        con = db.conectar()
        try:
            with con.cursor() as cursor:
                sql = """
                    SELECT u.id, u.usuario, u.password, t.nombre AS tipo, u.fecha_creacion, u.ultima_modificacion
                    FROM usuarios u
                    INNER JOIN tipos_usuario t ON u.tipo_usuario_id = t.id
                    WHERE u.id = %s
                """
                cursor.execute(sql, (id_usuario,))
                return cursor.fetchone()
        finally:
            db.cerrar()

    def modificar_usuario(self, id_usuario, nuevo_usuario, nuevo_password, nuevo_tipo):
        db = Conexion()
        con = db.conectar()
        try:
            with con.cursor() as cursor:
                cursor.execute("SELECT id FROM tipos_usuario WHERE nombre = %s", (nuevo_tipo,))
                rol = cursor.fetchone()
                if not rol: return False
                
                sql = "UPDATE usuarios SET usuario=%s, password=%s, tipo_usuario_id=%s WHERE id=%s"
                cursor.execute(sql, (nuevo_usuario, nuevo_password, rol['id'], id_usuario))
                con.commit()
                return cursor.rowcount > 0
        finally:
            db.cerrar()

    def eliminar_usuario(self, id_usuario):
        db = Conexion()
        con = db.conectar()
        try:
            with con.cursor() as cursor:
                cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
                con.commit()
                return cursor.rowcount > 0
        finally:
            db.cerrar()

    def contar_total_usuarios(self):
        db = Conexion()
        con = db.conectar()
        try:
            with con.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) as total FROM usuarios")
                return cursor.fetchone()['total']
        finally:
            db.cerrar()