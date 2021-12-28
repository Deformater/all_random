from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    nav_item_active_dict = {'index': 'active', 'coin': '', 'password': ''}
    return render_template('index.html', nav_item_active_dict=nav_item_active_dict)


@app.route("/coin")
def coin():
    nav_item_active_dict = {'index': '', 'coin': 'active', 'password': ''}
    return render_template('coin.html', nav_item_active_dict=nav_item_active_dict)


@app.route("/password")
def password():
    nav_item_active_dict = {'index': '', 'coin': '', 'password': 'active'}
    return render_template('password.html', nav_item_active_dict=nav_item_active_dict)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)