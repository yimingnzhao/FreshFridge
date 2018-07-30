from google.appengine.ext import ndb
import datetime

class FoodItem(ndb.Model):
    food_type = ndb.StringProperty(required=True)
    food_name = ndb.StringProperty(required=True)
    x = datetime.datetime.now()
    buy_month = ndb.IntegerProperty(default=x.month)
    buy_date = ndb.IntegerProperty(default=x.day)
    buy_year = ndb.IntegerProperty(default=x.year)
    exp_month = ndb.IntegerProperty(required=True)
    exp_date = ndb.IntegerProperty(required=True)
    exp_year = ndb.IntegerProperty(required=True)
