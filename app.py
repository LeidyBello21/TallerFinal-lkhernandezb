from flask import Flask, jsonify

# Clases de los animales
class AnimalExotico:
    def __init__(self, nombre, peso, pais_origen, impuestos):
        self.nombre = nombre
        self.peso = peso
        self.pais_origen = pais_origen
        self.impuestos = impuestos

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Huron(AnimalExotico):
    def hacer_sonido(self):
        return "¡Eek Eek!"

class BoaConstrictor(AnimalExotico):
    def __init__(self, nombre, peso, pais_origen, impuestos):
        super().__init__(nombre, peso, pais_origen, impuestos)
        self.ratones_comidos = 0

    def hacer_sonido(self):
        return "¡Tsss!"

class Perro(Animal):  
    def hacer_sonido(self):
        return "¡Guau Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"

# Instanciar animales
huron = Huron("Hurón Saltarín", 2.5, "México", 15.0)
boa = BoaConstrictor("Boa Feroz", 20.0, "Brasil", 25.0)
perro = Perro("Firulais")
gato = Gato("Michi")

# Crear la app Flask
app = Flask(__name__)

# Rutas del API
@app.route('/animal/huron', methods=['GET'])
def huron_sonido():
    return jsonify({"animal": "Hurón", "sonido": huron.hacer_sonido()})

@app.route('/animal/boa', methods=['GET'])
def boa_sonido():
    return jsonify({"animal": "Boa Constrictor", "sonido": boa.hacer_sonido()})

@app.route('/animal/perro', methods=['GET'])
def perro_sonido():
    return jsonify({"animal": "Perro", "sonido": perro.hacer_sonido()})

@app.route('/animal/gato', methods=['GET'])
def gato_sonido():
    return jsonify({"animal": "Gato", "sonido": gato.hacer_sonido()})

# Página principal
@app.route('/')
def home():
    return """
    <h1>API de Animales</h1>
    <p>Animales disponibles:</p>
    <ul>
        <li><a href="/animal/huron">Hurón</a></li>
        <li><a href="/animal/boa">Boa Constrictor</a></li>
        <li><a href="/animal/perro">Perro</a></li>
        <li><a href="/animal/gato">Gato</a></li>
    </ul>
    """

# Ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)
