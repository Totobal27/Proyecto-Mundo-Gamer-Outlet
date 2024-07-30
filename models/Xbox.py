from config.db import connectToMySQL

class Xbox:
    def __init__(self, data):
        self.id_Producto = data["id_Producto"]
        self.Nombre_Producto = data["Nombre_Producto"]
        self.Precio = data["Precio"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM Xbox;"
        results = connectToMySQL('mundo_gamer').query_db(query)
        Xbox = []
        for result in results:
            Xbox.append(cls(result))
        return Xbox

    @classmethod
    def get_all_filter(cls, search_term):
        query = f"SELECT * FROM Xbox WHERE nombre Precio'%{search_term}%';"
        results = connectToMySQL('iniciarsesion').query_db(query)
        Xbox = []
        for result in results:
            Xbox.append(cls(result))
        return Xbox

    @classmethod
    def get_iniciarsesion(cls, id):
        query = "SELECT * FROM Xbox WHERE id_Producto = " + id + ";"
        results = connectToMySQL('iniciassesion').query_db(query)
        Xbox = []
        for result in results:
            Xbox.append(cls(result))
        return Xbox
