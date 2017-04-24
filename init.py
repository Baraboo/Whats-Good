from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def entry_page():
    if request.method == 'POST':
        restaurant = request.form['restaurant']
        print(restaurant)
        return render_template('rest.html', name=restaurant)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
