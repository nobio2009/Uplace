import requests
from flask import Flask, redirect, render_template
app = Flask(__name__)

# Modes
def test(app, host, port):
    app.run()


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/meme')
def meme():
    res = requests.get('https://meme-api.com/gimme/cursedimages')
    return render_template('meme.html')

if __name__ == '__main__':
    app.run()
