from flask import Flask, render_template
import os
from db_schema import db

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db.init_app(app)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)