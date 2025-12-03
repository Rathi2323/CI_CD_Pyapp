from flask import Flask, jsonify
import os
import time

app = Flask(__name__)
start_time = time.time()

VERSION = os.getenv("APP_VERSION","1.0.0")
COMMIT = os.getenv("GIT_COMMIt","local")

@app.route("/")
def dashboard(): 
    return """
    <h2>DevOps Dashboard</h2>
    <u1>
        <li><a href="/hello">Hello API</a></li>
        <li><a href="/health">Health Check</a></li>
        <li><a href="/info">Build Info</a></li>
        <li><a href="/metrics">Metrics</a></li>
    <u1>
    """

@app.route("/hello")
def hello():
    return jsonify(message="Hello DevOps!")

@app.route("/health")
def health():
    return jsonify(status="UP"), 200

@app.route("/info")
def info():
    return jsonify(
        version = VERSION,
        commit = COMMIT,
    )

@app.route("/metrics")
def metrics():
    uptime = int(time.time()-start_time)
    
    return f"""
 # HELP app_uptime_seconds Application uptime in seconds
 # TYPE app_uptime_seconds counter
 app_uptime_seconds {uptime}
 """

if __name__ ==  "__main__":
    app.run(host="0.0.0.0", port = 5000)



