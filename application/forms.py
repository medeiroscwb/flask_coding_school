from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from application.models import User

class LoginForm(FlaskForm):
    email       = StringField("Email:", validators=[DataRequired(), Email()])
    password    = PasswordField("Password:", validators=[DataRequired(), Length(min=6, max=255)])
    remember_me = BooleanField("Remember Me")
    submit      = SubmitField("Login")

class RegisterForm(FlaskForm):
    email               = StringField("Email:", validators=[DataRequired(), Email()])
    password            = PasswordField("password", validators=[DataRequired(), Length(min=6, max=255)])
    password_confirm    = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=6, max=255), EqualTo('password')])
    first_name          = StringField("First Name", validators=[DataRequired(), Length(min=2,max=64)])
    last_name           = StringField("Last Name", validators=[DataRequired(), Length(min=2,max=64)])
    submit              = SubmitField("Register")

    def validate_email(self,email):
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("This email adress is already in use, Please pick another one.")

