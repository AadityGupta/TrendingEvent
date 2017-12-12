from djangotoolbox.fields import ListField, DictField
from django.db import models
from django_mongodb_engine.contrib import MongoDBManager

class Tweet(models.Model):
    data = DictField()
    objects = MongoDBManager()
