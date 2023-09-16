from flask import Flask, render_template
from controller import index as index_controller

app = Flask(__name__)


@app.get('/')
def index():  # put application's code here
    page = index_controller()
    return render_template("index.html", content=page)


if __name__ == '__main__':
    app.run()
