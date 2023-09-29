from flask import render_template, request, url_for, flash, redirect
from app import app


items = [
    {"product": "Laptop", "price": 799.99},
    {"product": "Smartphone", "price": 599.99},
    {"product": "Tablet", "price": 299.99},
    {"product": "Headphones", "price": 149.99},
    {"product": "Monitor", "price": 249.99},
    {"product": "Keyboard", "price": 49.99},
    {"product": "Mouse", "price": 19.99},
    {"product": "External Hard Drive", "price": 89.99},
    {"product": "Router", "price": 79.99},
    {"product": "Printer", "price": 129.99},
    {"product": "Webcam", "price": 69.99},
    {"product": "USB Flash Drive", "price": 9.99},
    {"product": "Graphics Card", "price": 399.99},
    {"product": "SSD", "price": 129.99},
    {"product": "Bluetooth Speaker", "price": 69.99},
    {"product": "Gaming Console", "price": 299.99},
    {"product": "Wireless Earbuds", "price": 149.99},
    {"product": "Camera", "price": 449.99},
    {"product": "VR Headset", "price": 349.99},
    {"product": "Smartwatch", "price": 199.99},
]



@app.route('/', endpoint='home')
def index():
    return render_template('index.html', items=items)


@app.route('/items/', methods=('GET', 'POST'), endpoint='items_page')
def add_items():
    if request.method == 'POST':
        item = request.form['item']
        price = request.form['price']

        if not item:
            flash('Item name is required!')
        elif not price:
            flash('Price is required!')
        else:
            items.append({'product': item, 'price': price})
            return redirect(url_for('home'))

    return render_template('add_items.html')







