from flask import Flask, render_template, request
from models.iniciarsesion import Iniciarsesion
app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/carrito')
def carrito():
    return render_template('carrito.html')

@app.route('/AcercaDe')
def AcercaDe():
    return render_template('AcercaDe.html')

@app.route('/nintendo')
def nintendo():
    return render_template('nintendo.html')

@app.route('/Playstation')
def Playstation():
    return render_template('Playstation.html')

@app.route('/QuienesSomos')
def QuienesSomos():
    return render_template('QuienesSomos.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/usuario')
def usuario():
    return render_template('usuario.html')

@app.route('/Xbox')
def Xbox():
    return render_template('Xbox.html')










if __name__ == '__main__':
    app.run(debug=True)
