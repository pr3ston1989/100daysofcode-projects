from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField

class RegisterForm(FlaskForm):
    username = StringField(label="Username:", validators=[DataRequired()])
    email = StringField(label="e-mail:", validators=[DataRequired(), Email()])
    fname = StringField(label="First name:")
    mname = StringField(label="Middle name:")
    lname = StringField(label="Last name:")
    password = PasswordField(label="Password:", validators=[DataRequired()])
    submit = SubmitField("Register")