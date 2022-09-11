from flask import Flask, render_template as render
from config import *


app = Flask(__name__)


@app.get("/")
def index():
    return render("base.html")


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
