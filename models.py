import datetime
from flask import url_for
from pros_and_cons import db
from slugify import slugify

class Pro(db.EmbeddedDocument):
  created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
  body = db.StringField(required=True)
  # priority = db.IntField(default=0, min_value=0, max_value=5, required=True)

class Con(db.EmbeddedDocument):
  created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
  body = db.StringField(required=True)
  # priority = db.IntField(default=0, min_value=0, max_value=5, required=True)

class List(db.Document):
  created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
  name = db.StringField(max_length=255, required=True)
  slug = db.StringField(unique=True)
  pros = db.ListField(db.EmbeddedDocumentField('Pro'))
  cons = db.ListField(db.EmbeddedDocumentField('Con'))

  def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.name)
    ret = super(List, self).save(*args, **kwargs)

  def get_absolute_url(self):
    return url_for('list', kwargs={"slug": self.slug})

  def __unicode__(self):
    return self.name

  meta = {
    'allow_inheritance': True,
    'indexes': ['-created_at', 'slug'],
    'ordering': ['-created_at']
  }