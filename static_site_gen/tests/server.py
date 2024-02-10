from flask import Flask, send_file
from pathlib import Path

app = Flask(__name__, root_path="./static_site_gen/tests/")


@app.route("/")
def index():
    return send_file(f"{Path(__file__).parent.absolute()}/index.html")


@app.route("/templates/style.css")
def style():
    return send_file(f"{Path(__file__).parent.absolute()}/templates/style.css")
