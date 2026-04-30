from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/prices')
def prices():
    return render_template('prices.html')


@app.route('/photos')
def photos():
    return render_template('photos.html')


if __name__=='__main__':
    app.run(host="0.0.0.0", port=10000)