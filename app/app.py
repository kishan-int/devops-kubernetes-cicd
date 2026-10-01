from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Hello from my DevOps application v2!",
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENVIRONMENT", "local")
    }

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)