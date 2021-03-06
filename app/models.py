from app import db
from markdown import markdown
from datetime import datetime
import bleach

class Post(db.Model):
    __tablename__="posts"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(64))
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    summury=db.Column(db.Text)
    summury_html=db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    category_id=db.Column(db.Integer,db.ForeignKey('categorys.id'))

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
                allowed_tags = ['a', 'abbr', 'acronym', 'b', 'code', 'blockquote','em', 'i',
                                'strong','li','ol','pre','strong','ul','h1','h2','h3','p']
                target.body_html = bleach.linkify(bleach.clean(
                        markdown(value, output_format='html'),
                        tags=allowed_tags, strip=True)
    )

    @staticmethod
    def on_changed_summury(target, value, oldvalue, initiator):
                allowed_tags = ['a', 'abbr', 'acronym', 'b', 'code', 'blockquote','em', 'i',
                                    'strong','li','ol','pre','strong','ul','h1','h2','h3','p']
                target.summury_html = bleach.linkify(bleach.clean(
                        markdown(value, output_format='html'),
                        tags=allowed_tags, strip=True)
                )


db.event.listen(Post.body, 'set', Post.on_changed_body)
db.event.listen(Post.summury, 'set', Post.on_changed_summury)

class Category(db.Model):
    __tablename__="categorys"
    id=db.Column(db.Integer,primary_key=True)
    tag=db.Column(db.String(64))
    count=db.Column(db.Integer)
    posts=db.relationship("Post",backref="category")