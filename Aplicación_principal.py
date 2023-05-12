from flask import Flask, request, render_template
from clases.jerarquia_clases import Piano, Trompeta, Violin

app = Flask(__name__,template_folder='html')

@app.route("/")
def instrumentosmusicales():
    return render_template("start_instrumentosmusicales.html")

@app.route("/instrumentosmusicales", methods=['POST'])
def mostrar_instrumentosmusicales():
    instrumentomusical = request.form["instrumentoMusical"]

    if instrumentomusical == "piano":
        variable = request.form["precio"]
        instrumentomusical_ingresado = Piano(instrumentomusical,request.form["precio"],  request.form["marca"])

    elif instrumentomusical == "trompeta":
        instrumentomusical_ingresado = Trompeta(instrumentomusical,request.form["precio"], request.form["tipo_trompeta"])

    elif instrumentomusical == "violin":
        instrumentomusical_ingresado = Violin(instrumentomusical,request.form["precio"], request.form["tipo_violin"])


 # Insertar el código aquí
        
 # Renderizar la página de instrumentos musicales con el instrumento musical seleccionado
    return render_template("instrumentosmusicales.html", instrumentoMusical=instrumentomusical_ingresado)


if __name__ == '__main__':
   app.run(debug=True)