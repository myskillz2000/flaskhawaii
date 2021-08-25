from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello from Hawaii!</h1>"

@app.route('/info')
def info():
    return "<h1>This was our honeymoon.</h1>"

@app.route('/some_page/<name>')
def some_page(name):
    return "<h1>This is an example of dynamic route{}</h1>".format(name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)