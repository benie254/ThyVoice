from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField, SelectField
from wtforms.validators import InputRequired


class BlogForm(FlaskForm):
    """
    creates new pitch objects
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
