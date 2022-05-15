from flask import render_template,redirect,url_for,request,abort
from . import main
from flask_login import login_required,current_user
from .. import db,photos
from ..models import User,Blog,Comment
from .forms import BlogForm,CommentForm


# views
@main.route('/', methods=['GET', 'POST'])
def index():
    """
    :return: index page + data
    """

    title = 'ThyVoice- Welcome!'

    blogs = Blog.query.all()
    comment_form = CommentForm()
    comments = Comment.query.all()

    if comment_form.validate_on_submit():
        comment_message = comment_form.comment.data
        comment = Comment(comment_message=comment_message)

        db.session.add(comment)
        db.session.commit()

        return redirect(url_for('.index'))

    return render_template('index.html',title=title,blogs=blogs,comments=comments)


@main.route('/user/<uname>')
def profile(uname):

    user = User.query.filter_by(username=uname).first()
    user_id = current_user._get_current_object().id
    user_blogs = Blog.query.filter_by(user_id=user_id).all()

    if user is None:
        abort(404)

    return render_template('profile/profile.html',user=user,user_blogs=user_blogs)


@main.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    """
    :return: index page + data
    """

    blogs = Blog.query.all()
    blog_form = BlogForm()

    if blog_form.validate_on_submit():
        blog_title = blog_form.blog_title.data
        blog_category = blog_form.blog_category.data
        blog_content = blog_form.blog_content.data
        user_id = current_user._get_current_object().id

        new_blog_dict = Blog(blog_title=blog_title, user_id=user_id, blog_category=blog_category,
                               blog_content=blog_content)

        new_blog_dict.save_blog()

        return redirect(url_for('main.index'))

    title = 'Create Blog- ThyVoice!'

    return render_template('create.html',title=title,blogs=blogs,blog_form=blog_form)




