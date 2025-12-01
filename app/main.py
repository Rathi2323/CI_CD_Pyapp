from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return {"Message":"Hello Devops!"}

@app.route("/health")
def health():
    return {"Status":"up"}

@app.route("/info")
def info():
    return {"version":"1.2","commit":"abc123"}

@app.route("/metrics")
def metrics():
    return "Promethus-ready metrics"

if __name__ ==  "__main__":
    app.run(host="0.0.0.0", port = 5000)



