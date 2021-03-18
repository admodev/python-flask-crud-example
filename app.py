from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)


@app.route('/ping')
def ping():
    return jsonify({"message": "Pong!"})


@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "Products list"})


@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [
        product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"Product": productsFound[0]})
    else:
        return jsonify({"Message": "Product not found!"})


@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }

    products.append(new_product)

    return jsonify({"message": "Product added successfully!", "products": products})


@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [
        product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Product Updated',
            'product': productsFound[0]
        })
    else:
        return jsonify({'message': 'Product Not found'})


@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [
        product for product in products if product['name'] == product_name
    ]
    if (len(productsFound) > 0):
        products.remove(productsFound[0])
        return jsonify({"message": "Product removed", "Products": products})
    else:
        return jsonify({"message": "Product not found!"})


if __name__ == '__main__':
    app.run(debug=True)
