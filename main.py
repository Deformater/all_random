from flask import Flask, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']


@app.route("/")
@app.route("/number")
def index():
    nav_item_active_dict = {'index': 'active', 'coin': '', 'password': ''}
    return render_template('number.html', nav_item_active_dict=nav_item_active_dict)


@app.route("/coin")
def coin():
    nav_item_active_dict = {'index': '', 'coin': 'active', 'password': ''}
    return render_template('coin.html', nav_item_active_dict=nav_item_active_dict)


@app.route("/password")
def password():
    nav_item_active_dict = {'index': '', 'coin': '', 'password': 'active'}
    return render_template('password.html', nav_item_active_dict=nav_item_active_dict, password='dfgd')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)
