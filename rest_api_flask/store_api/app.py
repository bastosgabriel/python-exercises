from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': "Lojinha",
        'items': [
            {
                'name': "Meu item",
                'price': 20.99
            },
            {
                'name': "Meu segundo item",
                'price': 30.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')


# GET /store
@app.route('/store')
def get_all_stores():
    return jsonify({'stores': stores})


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'].lower() == name.lower():
            return jsonify(store)
    return jsonify({'message': "Store not found"})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items(name):
    for store in stores:
        if store['name'].lower() == name.lower():
            return jsonify({'items': store['items']})
    return jsonify({'message': "Store not found"})


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'].lower() == name.lower():
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': "Store not found"})


# POST /store data: {name:}
@app.route('/store', methods = ['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)



app.run(port=5000)