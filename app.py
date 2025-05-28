#Código del servicio web Flask

#sirve un archivo .html (html es el framework que utiliza el front end, las páginas de internet con él exponen su contenido)
from flask import Flask, render_template, request

#levanta la app en flask, es una app que ya da la librería por default para ser consumida por el servicio
app = Flask(__name__)

#decorador: @app.route('/')
# ('/') es el path. Al levantar un sw, este nos da una url que es el servidor al que voy a ir a pegarle (por ej. google.com)
@app.route('/home', methods=["POST", "GET"])
#cada ruta es un método o función diferente que hará algo. Aquí faltó definir qué métodos que van a recibir la petición
# si consulto la ruta tal cual como "@app.route('/')", arroja error. Hay que agregarle el path que queramos consultar, por ejemplo, /"home"
# tmb agregamos los métodos que recibirán la petición: ent. cuando llegue una petición POST o una GET, en ambas se hará lo de la función de "home" con el path "/home"
def home(): #esta función es lo se va a ejecutar
    return render_template('index.html') #función que permite renderizar el contenido HTML que estamos exponiendo aquí



@app.route('/webhook', methods=["POST", "GET"])
def webhook():
    data = request.get_json()
    print (data) #? por qué no imprime data en postman, pero sí en la terminal
    #return("OK")
    edad = data.get("Edad")
    edad = edad * 12
    
    return f"Tu edad en meses es {edad} meses"

if __name__ == '__main__':
    app.run(debug=True) # debug=True significa que cualquier cambio que yo haga en el código, al darle cmnd + S, lo toma automatico y vuelve a cargar el servidor.

#definimos otro método que se llame webhook. y cambiaremos la función para consumirla a través de un json.
# de request (mpetodo propio de la librería flask), traete el .get_json()

# lo ideal: probar en postman
# las urls en un navegador, siempre mandan el método GET

#el return es lo que vamos a ver de respuesta del servicio

"""pensar en:
- el performance del servicio
- el manejo de errores/excepciones


Flask ya toma automáticos los códigos de respuesta.
"""

"""
requirements.txt
con él instalaré las librerías que necesito en un container con docker.
con el pip freeze > requirements.txt
Me dice: estas son las librerías que necesitas para poder correr este código.

Lo idea es probar en local y después exponerlo a traves de una nube o de un servicio en una nube

Una vez lista y construida la app o el servicio web. Ahora viene exponerlo en un servicio para que la gente a través de internet, pueda consumirlo.

¿Cómo hacer eso?
- subir el code a github (por buenas prácticas)
- crear una función

1. En Cloud build > Triggers > Create repository  creamos la conexión
2. En github.com creamos un repo nuevo con la config default, y nos ponemos como owner
3. Crear una copia local (que ahora se vea en Github Desktop) para subir los archivos
4. Copio los archivos que creamos a la carpeta de mi repo
5. Crear un archivo .dockerignore. "Dame el contenido de un gitignore" a ChatGPT y con eso lo poblo. Este archivo ignorará lo que le pase ahí: entornos virutlaes, archivos de dependencia, etc.
Los debe ignorar pa que no se vayan a github, y no utilizar espacio en mi github.

Los archivos que no se subirán, se ponen en letras muy claritas.
Ej: *.py eso ignora todo archivo de extensión python

42.25

"""

