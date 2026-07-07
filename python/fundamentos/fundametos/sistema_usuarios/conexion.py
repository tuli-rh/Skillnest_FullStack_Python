import pymysql

class Conexion:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"      # Tu usuario de MySQL
        self.password = ""      # Tu contraseña de MySQL
        self.db = "usuarios_db"
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db,
                cursorclass=pymysql.cursors.DictCursor
            )
            return self.conexion
        except pymysql.MySQLError as e:
            print(f"\x1b[31m[Error de Conexión]: {e}\x1b[0m")
            return None

    def cerrar(self):
        if self.conexion:
            self.conexion.close()