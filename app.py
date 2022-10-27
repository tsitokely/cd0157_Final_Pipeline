from flask import Flask
APP = Flask(__name__)


@APP.route('/')
def hello_world():
    return 'Hello, This is truly the best flask app ever!\n'



if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
