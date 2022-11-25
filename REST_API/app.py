import uuid
from flask import Flask, request
from flask_smorest import abort
from db import items, stores

app = Flask(__name__)

# retorna todas as lojas e seus itens
@app.get("/store")
def get_all_stores():
    return {"stores": list(stores.values())}


# retorna uma loja em específico e seus itens
@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found.")

# retorna os itens de uma loja em específico
@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found.")

# retorna todos os itens da base de dados
@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}

# recebe uma nova loja
@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store, 201

# recebe novos itens em uma loja já existente
@app.post("/item")
def create_item():
    item_data = request.get_json()

    if(
        "price" not in item_data
        or "store_id" not in item_data
        or "name" not in item_data
    ):
        abort(
            400, 
            message="Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload.",
        )

    if item_data["store_id"] not in stores:
        abort(404, message="Store not found.")

    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    item[item_id] = item

    return item, 201