from flask import Flask
import flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<p>helo Word</p>"


@app.route('/contato')
def contatos():
    return "<p>Contatos</p>"


    



if __name__ == '__main__':
    app.run( debug=True)