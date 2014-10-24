import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
# model is basically a database table containing information,
# instance of a model is a row of that table,
# column of that table is e.g. models.CharField()

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')

    #Return String representation of this object
    def __unicode__(self):
        return self.question_text

    #Create a method to check if Question was published recently
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question)  # Tells that choice is related to single Question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    #Return String representation of this object
    def __unicode__(self):
        return self.choice_text
