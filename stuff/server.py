from flask import Flask

app = Flask(__name__)
app.url_map.host_matching = True


@app.route('/', host='<host>')
def index(host):
    if 'deployrun.com' in host:
        return '<body><h2>It is flask domain-specific page.</h2></body>'
    return '<body>Hello world. <a href="/about/">About this page</a>.</body>'


@app.route('/about/', host='<host>')
def about(host):
    return f'<body>This is the about page for {host}</body>'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
