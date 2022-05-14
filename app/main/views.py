from flask import render_template,redirect,url_for,request,abort
from . import main
from flask_login import login_required,current_user
from .. import db,photos
from ..models import User


# views
@main.route('/', methods=['GET', 'POST'])
def index():
    """
    :return: index page + data
    """

    title = 'ThyVoice- Welcome!'

    return render_template('index.html',title=title)


@main.route('/user/<uname>')
def profile(uname):

    user = User.query.filter_by(username=uname).first()
    user_id = current_user._get_current_object().id

    if user is None:
        abort(404)

    return render_template('profile/profile.html',user=user)




