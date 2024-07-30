from config.db import connectToMySQL

class Nintendo:
    def __init__(self, data):
        self.id_Producto = data["id_Producto"]
        self.Nombre_Producto = data["Nombre_Producto"]
        self.Precio = data["Precio"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM Nintendo;"
        results = connectToMySQL('mundo_gamer').query_db(query)
        Nintendo = []
        for result in results:
            Nintendo.append(cls(result))
        return Nintendo

    @classmethod
    def get_all_filter(cls, search_term):
        query = f"SELECT * FROM Nintendo WHERE nombre Precio '%{search_term}%';"
        results = connectToMySQL('iniciarsesion').query_db(query)
        Nintendo = []
        for result in results:
            Nintendo.append(cls(result))
        return Nintendo

    @classmethod
    def get_iniciarsesion(cls, id):
        query = "SELECT * FROM Nintendo WHERE id_Producto = " + id + ";"
        results = connectToMySQL('iniciassesion').query_db(query)
        Nintendo = []
        for result in results:
            Nintendo.append(cls(result))
        return Nintendo
