import psycopg2

class Conexion:

    """ Metodo constructor
    """
    def __init__(self):
        self.con= psycopg2.connect("bdname=veterinaria-db user=postgres")

    """ getConexion

        rettorna la instancia de la base de datos
    """
    def getConexion(self):
        return self.con