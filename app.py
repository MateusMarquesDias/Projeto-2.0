from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Docker Stack!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    app.run(host='0.0.0.0', port=8000)
