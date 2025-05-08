from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    inventory = [
        {'item': 'Laptop', 'quantity': 10},
        {'item': 'Mouse', 'quantity': 25},
        {'item': 'Keyboard', 'quantity': 15}
    ]
    return render_template('index.html', inventory=inventory)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
