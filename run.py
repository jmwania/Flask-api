from flask import Flask, jsonify, make_response

app = Flask(__name__)

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
def orders():
    return make_response(jsonify(
            {
            'status' : "ok",
            'Message' : "Sucess",
            'My orders': orders
            }), 200)


if __name__ == '__main__':
    app.run(debug=True)