from flask import Flask, jsonify, request, session
from collections.abc import Iterable

app = Flask(__name__)

results = []

def flatten_list(nested_list):
    """ Elimina las listas anidadas recursivamente. 

    Recorre todos los elementos de la lista, y se llama a si misma
    usando como argumento cada elemento recorrido. Si los elementos
    no son iterables, se retornan. De otro modo se repite el recorrido,
    hasta unicamente tener elementos no iterables, es decir, no listas.

    Parameters
    ----------

    nested_list : list
        Lista con listas anidadas

    Returns
    -------
    list
        Lista con todos los elementos, de todas las listas

    """

    if isinstance(nested_list, Iterable):
        return [a for i in nested_list for a in flatten_list(i)]
    else:
        return [nested_list]

@app.route('/flat_list', methods=['POST'])
def flat_list():
    """
    Recibe por el metodo POST, un documento JSON. Con la lista anidada.

    Returns
    -------
    JSON
        Documento JSON con la lista aplanada.
    """

    nested_items = request.get_json()
    flat_list = {"result" : flatten_list(nested_items["items"])}
    if nested_items['save'] == 1:
        results.append({'items':nested_items['items'],'result':flat_list['result']})
    
    return jsonify(flat_list)

@app.route('/show_saved', methods=['GET'])
def show_saved():
    """
    Returns
    -------
    JSON
        Documento JSON con las listas antes y después de aplanarse.
    """
    return jsonify(results)


if __name__ == '__main__':
    app.run()