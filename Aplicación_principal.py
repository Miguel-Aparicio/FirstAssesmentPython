from flask import Flask, request, render_template

app = Flask(__name__,template_folder='Páginas_Web.html')

@app.route("/")
def instrumentosmusicales():
    return render_template("start_instrumentosmusicales.html")

@app.route("/instrumentosmusicales", methods=['POST'])
def mostrar_instrumentosmusicales():
 # Obtener la instrumentoMusical seleccionada por el usuario

 # Insertar el código aquí
        
 # Renderizar la página de instrumentos musicales con el instrumento musical seleccionado
 return render_template("instrumentosmusicales.html", instrumentoMusical=instrumentoMusical_ingresado)


if __name__ == '__main__':
   app.run(debug=True)