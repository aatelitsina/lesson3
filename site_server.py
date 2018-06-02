from flask import Flask
from child_data_site import get_table_child

app = Flask(__name__)

@app.route("/name")
def index():
    return get_table_child()


if __name__ == "__main__":
    app.run()
