from flask import Flask, jsonify, make_response, request
#from flask_restful import API

app = Flask(__name__)
#api = API(app) 

orders = [
{
        'id': 1,
        'Description' : {"Item 1": "T-shirts", "Item 2" : "Pizza"}, 
        'price' : 600
},
{
        'id' : 2,
        'Description' : {"Item 1": "Trousers", "Item 2": "Bananas"},
        'Price': 1500
}
]

@app.route('/', methods= ['GET'])
def order():
    return make_response(jsonify(
            {
            'Status' : "ok",
            'Message' : "Sucess",
            'My orders': orders
            }), 403)

@app.route('/post', methods= ['POST'])
def post_order():

        data = request.get_json()
        id = leng(orders) +1
        item1 = data['item 1']
        item2 = data['item 2']
        price = data['price']


payload = {
'id': id,
'Description': {'Item 1': item1, 'Item 2': item2},
'Price': price
}
orders.append(payload)



if __name__ == '__main__':
    app.run(debug=True)