from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, widgets, FileField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired

class SignUp(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=30)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginPage(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=30)])
    submit = SubmitField('Login')

class Admin_Account(FlaskForm):
	acctype = SelectField('Account Type', choices=[('User', 'User'), ('Admin', 'Admin')], validators=[DataRequired()])
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=30)])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Create Account')

class Admin_EditPage(FlaskForm):
    acctype = SelectField('Account Type', choices=[('User', 'User'), ('Admin', 'Admin')], validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=30)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Account')

class Admin_Product(FlaskForm):
    categoryid = SelectField('Category Name', choices = [], validators=[DataRequired()])
    productname = StringField('Product Name', validators=[DataRequired()])
    productdesc = StringField('Product Description', validators=[DataRequired()])
    picture = FileField('Image File', validators=[FileRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    price = DecimalField('Price', places = 1, validators=[DataRequired()])
    submit = SubmitField('Create Product')