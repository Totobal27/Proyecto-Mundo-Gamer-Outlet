from config.db import connectToMySQL

class Playstation:
    def __init__(self, data):
        self.id_Producto = data["id_Producto"]
        self.Nombre_Producto = data["Nombre_Producto"]
        self.Precio = data["Precio"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM Playstation;"
        results = connectToMySQL('mundo_gamer').query_db(query)
        Playstation = []
        for result in results:
            Playstation.append(cls(result))
        return Playstation

    @classmethod
    def get_all_filter(cls, search_term):
        query = f"SELECT * FROM Nintendo WHERE nombre Precio '%{search_term}%';"
        results = connectToMySQL('iniciarsesion').query_db(query)
        Playstation = []
        for result in results:
            Playstation.append(cls(result))
        return Playstation

    @classmethod
    def get_iniciarsesion(cls, id):
        query = "SELECT * FROM Nintendo WHERE id_Producto = " + id + ";"
        results = connectToMySQL('iniciassesion').query_db(query)
        Playstation = []
        for result in results:
            Playstation.append(cls(result))
        return Playstation
