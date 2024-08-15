# Data access object - DAO

from conexion.Conexion import Conexion

class CiudadDao:

    def getCiudades(self):

        ciudadSql = """
    SELECT id, descripción
    FROM ciudades
    """
    # Objeto de conexion a la base de datos
    conexion = Conexion()
    con = conexion.getConexion()
    try:
        pass
    except:
        pass
    finally:
        pass