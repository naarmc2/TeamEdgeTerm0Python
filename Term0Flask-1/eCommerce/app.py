from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route("/")
def test():
    
    global products
    
    products = {
        "item1": {"ID": 12, "name": "bicycle", "price": 34, "description":"Usable and in great condition" },
        "item2": {"ID": 13, "name": "bag", "price": 23, "description":"Usable and in great condition" },
        "item3": {"ID": 14, "name": "shirt", "price": 12, "description":"Usable and in great condition"},
    }

    return render_template("index.html", products=products)

@app.route('/products/<productID>')

def productGenerator(productID):
    product = products.get(productID)
    if not product:
        abort(404)
    return render_template('index.html', product=product)
@app.route('/about')

def about():
    return render_template("about.html")
