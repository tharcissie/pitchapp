from flask_wtf import FlaskForm
from wtforms import ValidationError, SubmitField,BooleanField, StringField,PasswordField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class LoginForm(FlaskForm):
    username = StringField('Enter your Username...',validators=[Required()])
    password = PasswordField('Enter your Password...',validators=[Required()])
    remember = BooleanField('Remember Me!')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email = StringField('Enter your Email...', validators=[Required(),Email()])
    username = StringField('Enter Your Username...', validators=[Required()])
    password = PasswordField('Create a Password...',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm your Password...',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("Email not valiable")
    
    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError("Username not valiable")
