from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<body><h3 style="margin-top: 20%; text-align: center">Hello from the domain-specific page.</h3></body>'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
