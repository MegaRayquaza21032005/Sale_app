from saleapp import app
from flask import render_template
import utils
# from saleapp import utils (vscode)
# python3 -m saleapp.index

@app.route('/')
def home():
    cats = utils.load_categories()
    return render_template("index.html",
                           categories = cats)

@app.route("/products")
def product_list():
    products = utils.load_products()
    return render_template("products.html",
                           products = products)

if __name__ == '__main__':
    app.run(debug=True)