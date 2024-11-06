from flask import Flask, request

app = Flask(__name__)


@app.route("/VistaCategoria/<int:id>/<string:nombre>/<string:descripcion>", methods=['GET'])
def VistaCategoria(id, nombre, descripcion):
    app.logger.info(f'Solicitud a la ruta{request.path}')
    Categoria = {'id': id, 'nombre': nombre, 'descripcion': descripcion}
    return Categoria

@app.route("/NuevaCategoria/<id>/<nombre>/<descripcion>", methods=['POST'])
def NuevaCategoria(id, nombre, descripcion):
    app.logger.info(f'Solicitud a la ruta{request.path}')
    CategoriaNueva = {'id': id, 'nombre': nombre, 'descripcion': descripcion, 'metodo_http': request.method}
    return CategoriaNueva


@app.route("/EditarCategoria/<int:id>", methods=['PUT'])
def EditarCategoria(id):
        id = request.form.get('id')

        valor = {'id': id}
        return f'La categoria a editar es {valor}'



@app.route("/EliminarCategoria/<int:id>", methods=['DELETE'])
def delete(id):
    id = request.form.get(id)

    valores = {'id': id}
    return f'La categoria a eliminar es {valores}'

