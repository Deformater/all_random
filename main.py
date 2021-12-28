from flask import Flask, render_template, request
from flask_cors import CORS
from werkzeug.security import generate_password_hash
from settings import HOST
import requests


app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret_key'


@app.route("/")
@app.route("/index")
def index():
    nav_item_active_dict = {'index': 'active', 'coin': '', 'password': ''}
    return render_template('index.html', nav_item_active_dict=nav_item_active_dict)


@app.route("/coin")
def coin():
    nav_item_active_dict = {'index': '', 'coin': 'active', 'password': ''}
    return render_template('coin.html', nav_item_active_dict=nav_item_active_dict)


@app.route("/password", methods=['GET', 'POST'])
def password():
    nav_item_active_dict = {'index': '', 'coin': '', 'password': 'active'}
    if request.method == 'GET':
        return render_template('password.html', nav_item_active_dict=nav_item_active_dict, password='dfgd')
    elif request.method == 'POST':
        data_json = request.json
        length = data_json['length']
        is_number = data_json['numbers']
        is_spec_symbol = data_json['spec_symbols']

        # response = requests.get(f'{HOST}/password?length={length}&is_number={is_number}'
        #                         f'&is_spec_symbol={is_spec_symbol}')
        # if response.status_code != 200:
        #     return render_template('password.html', error=response.text)
        #
        # password = response.json()['password']

        password = generate_password_hash('aboba')
        return render_template('password.html', password=password, nav_item_active_dict=nav_item_active_dict)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)