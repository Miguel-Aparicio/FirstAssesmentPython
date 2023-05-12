from clases import jerarquia_clases
from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <!--start_instrumentosmusicales.html-->
    <!DOCTYPE html>
    <html>

    <head>
        <meta charset="UTF-8">
        <title>Información de la instrumentoMusical</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
        <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}" />
    </head>

    <body>
        <fieldset>
            <legend>Información de instrumentosmusicales</legend>
            <div class="form-group row">
                {% if instrumentoMusical %}
                <p><strong>Nombre:</strong> {{ instrumentoMusical.nombre }}</p>
                <p><strong>Precio:</strong> {{ instrumentoMusical.precio }}</p>
                {% if (instrumentoMusical.Nombre == "trompeta") %}
                <p><strong>Tipo trompeta:</strong> {{ instrumentoMusical.tipo_trompeta }}</p>
                {% elif (instrumentoMusical.Nombre== "piano") %}
                <p><strong>Marca:</strong> {{ instrumentoMusical.Marca }}</p>
                {% elif (instrumentoMusical.Nombre == "violín") %}
                <p><strong>Tipo violín:</strong> {{ instrumentoMusical.tipo_violin }}</p>
                {% endif %}
                <p><strong>Descripcion:</strong> {{ instrumentoMusical.descripcion() }}</p>
                {% else %}
                <p>La instrumentoMusical seleccionada no fue encontrada en la lista.</p>
                {% endif %}
                <form method="get" action="/">
                    <button type="submit" class="btn btn-primary">Mas instrumentosmusicales</button>
                </form>
            </div>
        </fieldset>
    </body>
    </html>

    <!-- start_instrumentosmusicales.html -->
    <!DOCTYPE html>
    <html>

    <head>
    <meta charset="UTF-8">
    <title>Información de instrumentosmusicales</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}" />
    </head>

    <body>
    <form method="post" action="/instrumentosmusicales">
        <legend>Información de instrumentosmusicales</legend>
        <fieldset  class="d-grid" >
        <label for="instrumentoMusical">Selecciona una instrumentoMusical:</label>
        <select id="instrumentoMusical" name="instrumentoMusical" class="col-form-label col-form-label-sm">
            <option value="trompeta">Trompeta</option>
            <option value="piano">Piano</option>
            <option value="violín">Violín</option>
        </select>
        <label for="precio" class="col-form-label col-form-label-sm">Precio:</label>
        <input type="number" id="precio" name="precio" >
        <div id="atributos">
            <label for="tipo_trompeta" class="col-form-label col-form-label-sm">Tipo trompeta:</label>
            <input type="text" id="tipo_trompeta" name="tipo_trompeta" >
        </div>
        </fieldset>
        <button type="submit" class="btn btn-primary">Revisar</button>
    </form>

    <script>
        const instrumentosmusicaleselect = document.getElementById("instrumentoMusical");
        const atributosDiv = document.getElementById("atributos");

        function mostrarAtributos() {
        const instrumentoMusical = instrumentosmusicaleselect.value;
        atributosDiv.innerHTML = "";

        if (instrumentoMusical === "trompeta") {
            atributosDiv.innerHTML += `
                <label for="tipo_trompeta" class="col-form-label col-form-label-sm">Tipo trompeta:</label>
            <input type="text" id="tipo_trompeta" name="tipo_trompeta" >
            `;
        } else if (instrumentoMusical === "piano") {
            atributosDiv.innerHTML += `
                <label for="marca" class="col-form-label col-form-label-sm">Marca:</label>
                <input type="text" id="marca" name="marca">
            `;
        } else if (instrumentoMusical === "violín") {
            atributosDiv.innerHTML += `
                <label for="tipo_violin" class="col-form-label col-form-label-sm">Tipo de Violín:</label>
                <input type="text" id="tipo_violin" name="tipo_violin">
            `;
        }
        }
        instrumentosmusicaleselect.addEventListener("change", mostrarAtributos);
    </script>
    </body>

    </html>
    """

if __name__ == "__main__":
    app.run()