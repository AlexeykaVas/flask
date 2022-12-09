from flask import Flask, render_template, redirect
from flask import request
import random
import string

app = Flask(__name__)

letters, length = string.ascii_lowercase, 6
rand_string = ''.join(random.choice(letters) for i in range(length))


@app.route('/')
def login():
    return f"""
        <form action="/main">
  URL: <input type="text" name="url">
  <button type="submit">
    OK
  </button>
</form>
    """


@app.route('/main')
def hi():
    global url
    url = request.args.get('url')
    return f"""
        <p>http://127.0.0.1:5000/{word()}</p>
        """


@app.route(f'/{rand_string}')
def random():
    return redirect(f"http://{url}", code=302)

if __name__ == '__main__':
    app.run()