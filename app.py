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

# pagina de error
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
