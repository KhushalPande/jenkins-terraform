import os
import socket

from flask import Flask, jsonify, request

app = Flask(__name__)

GREETING = "CI/CD with Jenkins - version 1"
BUILD = os.getenv("APP_VERSION", "local")


@app.route("/")
def home():
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>CI/CD Demo</title>
<style>
 body {{ font-family: Arial, sans-serif; background:#fdf6ec; text-align:center; padding-top:70px; }}
 .box {{ display:inline-block; background:#fff; padding:30px 50px; border-radius:12px;
         box-shadow:0 2px 10px rgba(0,0,0,.15); }}
 h1 {{ color:#b6451b; margin-top:0; }}
 .b {{ color:#2f7d32; font-size:1.4em; font-weight:bold; }}
</style></head>
<body><div class="box">
 <h1>{GREETING}</h1>
 <p>Deployed automatically by Jenkins</p>
 <p>Jenkins build number: <span class="b">#{BUILD}</span></p>
 <p>Container: {socket.gethostname()}</p>
</div></body></html>"""


@app.route("/health")
def health():
    return jsonify(status="ok", build=BUILD)


@app.route("/api/add")
def add():
    try:
        a = float(request.args.get("a", ""))
        b = float(request.args.get("b", ""))
    except ValueError:
        return jsonify(error="a and b must be numbers"), 400
    return jsonify(result=a + b)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
