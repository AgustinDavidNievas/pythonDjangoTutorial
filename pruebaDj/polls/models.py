import datetime
from django.utils import timezone
from django.db import models


# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('Date published')
    
    def __unicode__(self): #se usa __unicode__() en lugar de  __str__() por Django, la costumbre en python es usar__str__()
        return self.question
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
    
    was_published_recently.short_description = 'Published recently?'
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField()
    
    def __unicode__(self):
        return self.choice_text