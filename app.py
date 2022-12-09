from flask import Flask
from flask import request
app = Flask(__name__)
num_visits = 0
@app.route("/")
def hello_world():
    global num_visits
    num_visits += 1
    ip_addr = request.remote_addr
    name = request.args.get('name')
    return f"""
    <p>Hello, {name}</p>
    <p>Вы зашли {num_visits} раз</p>
    <p><a href="/goodbay">Next</a></p>
    <p>IP: {ip_addr}</p>
    <p> url: {request.url}</p>
    """
@app.route("/goodbay")
def bye():
    global num_visits
    num_visits += 1
    return """
    <p style='color:red;'>Goodbye!</p>
    """
app.run(host='0.0.0.0', port='1234')