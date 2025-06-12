from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import User, Category

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), 
        Length(min=3, max=64, message='Username must be between 3 and 64 characters')
    ])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(), 
        Length(min=6, message='Password must be at least 6 characters')
    ])
    password2 = PasswordField('Confirm Password', validators=[
        DataRequired(), 
        EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose a different one.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already registered. Please use a different email.')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired(), 
        Length(min=5, max=200, message='Title must be between 5 and 200 characters')
    ])
    summary = StringField('Summary', validators=[
        Length(max=300, message='Summary must not exceed 300 characters')
    ])
    content = TextAreaField('Content', validators=[
        DataRequired(), 
        Length(min=10, message='Content must be at least 10 characters')
    ])
    category_id = SelectField('Category', coerce=int, choices=[])
    submit = SubmitField('Publish Post')
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.category_id.choices = [(0, 'No Category')] + [(c.id, c.name) for c in Category.query.all()]

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[
        DataRequired(), 
        Length(min=5, max=1000, message='Comment must be between 5 and 1000 characters')
    ])
    submit = SubmitField('Add Comment')

class CategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[
        DataRequired(), 
        Length(min=3, max=64, message='Category name must be between 3 and 64 characters')
    ])
    description = TextAreaField('Description', validators=[
        Length(max=200, message='Description must not exceed 200 characters')
    ])
    submit = SubmitField('Create Category')
    
    def validate_name(self, name):
        category = Category.query.filter_by(name=name.data).first()
        if category:
            raise ValidationError('Category already exists. Please choose a different name.')
