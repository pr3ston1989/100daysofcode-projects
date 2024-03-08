from flask import Flask, render_template,request
from flask_bootstrap import Bootstrap5
import os
from datetime import datetime
from db_schema import db, User, BlogPost, PostComment, Category, PostCategory, Tag, PostTags
from forms import RegisterForm
from flask_ckeditor import CKEditor
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
Bootstrap5(app)
ckeditor = CKEditor(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        password_hash = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            login=request.form.get('username'),
            password_hash=password_hash,
            email=request.form.get('email'),
            first_name=request.form.get('fname'),
            middle_name=request.form.get('mname'),
            last_name=request.form.get('lname'),
            registered_at=datetime.now(),
            last_login=datetime.now(),
            intro=None,
            avatar=None,
            profile=None,
        )
        db.session.add(new_user)
        db.session.commit()
    return render_template("register.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)