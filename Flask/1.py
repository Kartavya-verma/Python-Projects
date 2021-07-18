from flask import Flask
app= Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/kv")
def hello_kv():
    return "Hello World KV"

app.run(debug=True)