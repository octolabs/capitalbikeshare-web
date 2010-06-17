from google.appengine.ext import db

class Survey(db.Model):
  data = db.StringProperty(multiline=True)
  circulator = db.StringProperty(multiline=False)
  commute = db.StringProperty(multiline=False)
  smartbike = db.StringProperty(multiline=False)
  cabi = db.StringProperty(multiline=False)
  email = db.StringProperty(multiline=False)
  date = db.DateTimeProperty(auto_now_add=True)
  
