from flask import Flask, render_template_string as render_str
from config import *


app = Flask(__name__)


@app.get("/")
def index():
    return render_str("<h1>KEZERO.COM</h1>")


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
