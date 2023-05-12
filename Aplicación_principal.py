from flask import Flask, request, render_template
from clases import jerarquia_clases

app = Flask(__name__,template_folder='html')

@app.route("/")
def instrumentosmusicales():
    return render_template("start_instrumentosmusicales.html")

@app.route("/instrumentosmusicales", methods=['POST'])
def mostrar_instrumentosmusicales():
    piano = request.form["Piano"]
    trompeta = request.form["Trompeta"]
    violin = request.form["Violín"]
    if piano == "Piano":
        variable = request.form["marca"]
        instrumentomusical_ingresado = piano()


 # Insertar el código aquí
        
 # Renderizar la página de instrumentos musicales con el instrumento musical seleccionado
    return render_template("instrumentosmusicales.html", instrumentoMusical=instrumentomusical_ingresado)


if __name__ == '__main__':
   app.run(debug=True)