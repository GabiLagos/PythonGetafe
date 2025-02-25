import oracledb
class conexionOracleEnfermos:
    #debemos crear un objeto connection para usarlo en todos los metodos (__init__)
    def __init__(self):
        self.connection= oracledb.connect(user='system', password='oracle', dsn='localhost/xe')
    
    def eliminarEnfermo(self, inscripcion):
        cursor=self.connection.cursor()
        sqldelete= "delete from enfermo where inscripcion=:p1"
        cursor.execute(sqldelete, (inscripcion,))
        registros=cursor.rowcount
        cursor.close()
        return registros
    def modificarEnfermo(self, apellido, inscripcion):
        cursor=self.connection.cursor()
        sqlupdate="update enfermo set apellido=:p1 where inscripcion=:p2"
        cursor.execute(sqlupdate, (apellido,inscripcion))
        registros=cursor.rowcount
        cursor.close()
        return registros