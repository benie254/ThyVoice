from flask import render_template,redirect,url_for,request,abort
from . import main
from flask_login import login_required,current_user
from .. import db,photos
from ..models import User,Blog,Comment
from .forms import BlogForm,CommentForm,UpdateProfile,UpdateBlog
from ..requests import get_quotes


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

    my_quotes = get_quotes()

    print(my_quotes)

    if comment_form.validate_on_submit():
        comment_message = comment_form.comment.data
        comment = Comment(comment_message=comment_message)

        db.session.add(comment)
        db.session.commit()

        return redirect(url_for('.index'))

    return render_template('index.html',title=title,blogs=blogs,comments=comments,comment_form=comment_form,my_quotes=my_quotes)


@main.route('/user/<uname>')
def profile(uname):

    user = User.query.filter_by(username=uname).first()
    user_id = current_user._get_current_object().id
    user_blogs = Blog.query.filter_by(user_id=user_id).all()

    if user is None:
        abort(404)

    return render_template('profile/profile.html',user=user,user_blogs=user_blogs)


@main.route('/user/<uname>/update',methods=['GET','POST'])
@login_required
def update_profile(uname):

    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    update_form = UpdateProfile()

    if update_form.validate_on_submit():
        user.bio = update_form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',user=user,update_form=update_form)


@main.route('/user/<user_id>/update',methods=['GET','POST'])
@login_required
def update_blog(user_id):

    # user = User.query.filter_by(username=uname).first()
    user_blog = Blog.query.filter_by(user_id=user_id).first()
    user_id = current_user._get_current_object().id
    user_blogs = Blog.query.filter_by(user_id=user_id).all()

    if user_blog is None:
        abort(404)

    update_blog = UpdateBlog()

    if update_blog.validate_on_submit():
        user_blog.blog_content = update_blog.blog_content.data

        db.session.add(user_blog)
        db.session.commit()

        return redirect(url_for('.profile',user_id=user_id,user_blog=user_blog,user_blogs=user_blogs))

    return render_template('profile/update_blog.html',user_id=user_id,user_blog=user_blog,user_blogs=user_blogs,update_blog=update_blog)


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




