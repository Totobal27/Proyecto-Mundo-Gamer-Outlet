from config.db import connectToMySQL

class Iniciarsesion:
    def __init__(self, data):
        self.id = data["id"]
        self.Usuario = data["Usuario"]
        self.contraseña = data["Contraseña"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM iniciarsesion;"
        results = connectToMySQL('mundo_gamer').query_db(query)
        iniciarsesion = []
        for result in results:
            iniciarsesion.append(cls(result))
        return iniciarsesion

    @classmethod
    def get_all_filter(cls, search_term):
        query = f"SELECT * FROM iniciarsesion WHERE nombre Usuario '%{search_term}%';"
        results = connectToMySQL('iniciarsesion').query_db(query)
        iniciarsesion = []
        for result in results:
            iniciarsesion.append(cls(result))
        return iniciarsesion

    @classmethod
    def get_iniciarsesion(cls, nombre, contra):
        query = "insert into (Usuarios, Contraseña) values (%s, %s);"
        results = connectToMySQL('iniciassesion').query_db(query,(nombre, contra))
        iniciarsesion = []
        for result in results:
            iniciarsesion.append(cls(result))
        return iniciarsesion
