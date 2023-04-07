from flask import Flask, request, jsonify

app = Flask(__name__)

items = [
    {"id":"1","name":"product name","category":"1","price":"20.5","instock":"200"},
    
]

def _find_next_id(id):
    data = [x for x in items if x['id']==id]
    return data

@app.route('/item/<int:id>', methods=["DELETE"])
def get_item(id: int):

    data = _find_next_id(id)
    if not data:
        return {"error": "Item not found"}, 404
    else:
        items.remove(data[0])
        return "Item removed successfully", 200

@app.route('/item/<int:id>', methods=["PATCH"])
def patch_item(id: int):
    id = request.form.get('id')
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    data = _find_next_id(id)
    if not data:
        return {"error": "Item not found"}, 404
    
    name.form.get('name')
    category.form.get('category')
    price.form.get('price')
    instock.form.get('instock')
    
    if name:
        data['name'] = name
    if category:
        data['category'] = category
    if price:
        data['price'] = price
    if category:
        data['instock'] = instock
    return {"message": "Item updated successfully"}, 200

@app.route('/item/<id>', methods=["GET"])
def get_item_id(id):
    data = _find_next_id(id)
    return jsonify(data)

@app.route('/item', methods=["GET"])
def get_item():
    return jsonify(items)

@app.route('/item/<id>', methods=["GET"])
def get_item_id(id):
    data = _find_next_id(id)
    return jsonify(data)

@app.route('/item', methods=["POST"])
def post_item():
    id = request.form.get('id')
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    new_data = {
        "id": id,
        "name": name,
        "category": category,
        "price": price,
        "instock": instock,
    }

    if (_find_next_id(id)):
        return {"error": "Bad Request"}, id
    else:
        items.append(new_data)
        return jsonify(items)

@app.route('/put_item/<int:i_id>', methods=["PUT"])
def update_item(i_id):
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    update_data = {
        "name": name,
        "category": category,
        "price": price,
        "instock": instock,
    }

    for item in items:
        if i_id == item.get("id"):
            item["name"] = str(name)
            item["category"] = str(category)
            item["price"] = str(price)
            item["instock"] = str(instock)
            return jsonify(items)
        
        else:
            return "Error", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
