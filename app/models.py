from app import db, login, ldap
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.filter('id:' + id).first()


class User(UserMixin, ldap.Entry):

    base_dn = 'ou=People,dc=ma5,dc=lliurex,dc=net'
    object_classes = ['posixAccount']
    id = ldap.Attribute('uidNumber')
    username = ldap.Attribute('uid')
    

    def check_password(self, password):
        return self.authenticate(password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#     def __repr__(self):
#         return '<Post {}>'.format(self.body)
