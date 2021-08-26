from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    mylist = ['Lihue', 'Waimea', 'Princeville', 'Napali Coast',
              'Smith Family Luau', 'Pearl Harbor/Polynesian Cultural Center',
              'Fern Grotto', 'Bali Hai Resort']
    return render_template('basic.html', locations=locations)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)