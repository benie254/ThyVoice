from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import UserMixin, current_user
from . import login_manager
from datetime import datetime


class User(UserMixin, db.Model):
    """
    defines User objects
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    blogs = db.relationship('Blog', backref='user', lazy='dynamic')
    blog_comment = db.relationship('Comment', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'Users {self.username}'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class Blog(db.Model):
    """
    defines Blog objects
    """

    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer)
    blog_title = db.Column(db.String(255))
    blog_description = db.Column(db.String(255))
    blog_content = db.Column(db.String(2500))
    blog_category = db.Column(db.String(255), index=True, nullable=False)
    blog_pic_path = db.Column(db.String())
    blog_date = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blog_comment = db.relationship('Comment', backref='blog', lazy='dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls, id):
        blogs = Blog.query.filter_by(pitch_id=id).all()
        return blogs


class Comment(db.Model):
    """
    defines Comment objects
    """

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment_message = db.Column(db.String(255))

    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    def __repr__(self):
        return f"Comment : id: {self.id} comment: {self.comment_message}"


class Quote:
    """
    defines Quote objects
    """

    __tablename__ = 'quotes'

    id = db.Column(db.Integer, primary_key=True)
    quote_id = db.Column(db.Integer)
    quote_author = db.Column(db.String(255))
    quote_message = db.Column(db.String(255))