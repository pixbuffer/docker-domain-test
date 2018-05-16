from flask import Flask, abort

app = Flask(__name__)
app.url_map.host_matching = True
allowed_domains = ['deploylink.com', 'deployrun.com']


@app.route('/', host='<host>')
def index(host):
    for domain in allowed_domains:
        if domain in host:
            return f'<body><h2>It is flask domain-specific page for {host}.</h2></body>'
    abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
