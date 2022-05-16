from flask_wtf import FlaskForm
from sqlalchemy import Integer
from wtforms import SubmitField, TextAreaField, StringField, SelectField, PasswordField
from wtforms.validators import InputRequired, Email, ValidationError
from ..models import User


class BlogForm(FlaskForm):
    """
    creates new blog objects
    """

    blog_title = StringField('Title')
    blog_content = TextAreaField('Blog content')
    blog_category = SelectField('Category', choices=['poetry', 'fiction', 'nonfiction', 'business', 'lifestyle','home&living','one-liners'])
    submit = SubmitField('Post blog')


class CommentForm(FlaskForm):
    """
    creates new comments
    """

    comment = TextAreaField('What are your thoughts on this?')
    submit = SubmitField('Share Comment')


class UpdateProfile(FlaskForm):
    """
    updates user profile
    """

    bio = TextAreaField('Tell us about you.', validators=[InputRequired()])
    submit = SubmitField('Update Profile')


class UpdateBlog(FlaskForm):
    """
    updates user blogs
    """

    blog_title = StringField('Title',validators=[InputRequired()])
    blog_content = TextAreaField('Blog content',validators=[InputRequired()])
    blog_category = SelectField('Category',
                                choices=['poetry', 'fiction', 'nonfiction', 'business', 'lifestyle', 'home&living',
                                         'one-liners'],validators=[InputRequired()])
    submit = SubmitField('Update blog')


class DeleteBlog(FlaskForm):
    """
    updates user blogs
    """

    blog_title = StringField('Title',validators=[InputRequired()])
    submit = SubmitField('Delete blog')


class SubscriptionForm(FlaskForm):
        """
        signs in existing users
        """
        email = StringField('Email...', validators=[InputRequired(), Email()])
        submit = SubmitField('Subscribe')
