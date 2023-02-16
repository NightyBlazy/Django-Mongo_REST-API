from mongoengine import Document, fields
import datetime

# Create your models here.


class TsunBlog(Document):
    title = fields.StringField(required=True)
    body = fields.StringField(required=True)
    preview = fields.StringField(required=True, max_length=30)
    author = fields.StringField(required=True)
    date = fields.StringField(required=True)
    meta = {'collection': 'blogs','strict': False}