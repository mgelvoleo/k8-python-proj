from flask import Flask
from socket import gethostname  # Import gethostname function

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Dockerized Flask App and the hostname was ' + gethostname()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
