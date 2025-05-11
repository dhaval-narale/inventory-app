from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    inventory = [
        {'item': 'Laptop', 'quantity': 10},
        {'item': 'Mouse', 'quantity': 25},
        {'item': 'Keyboard', 'quantity': 15}
    ]
    last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', inventory=inventory, last_updated=last_updated)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
