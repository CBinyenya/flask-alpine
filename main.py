from flask import Flask
import requests
app = Flask(__name__)

@app.route('/flask1/hello')
def hello_world():
    return 'Hello World! from flask1'

@app.route('/flask1')
def flask1():
	return 'I am flask 1'

@app.route('/greeting')
def greeting():
	r = requests.get('http://docker-node/flask2/hello')	
	return r.text

@app.route('/')
def root():
	return 'Root index'

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
