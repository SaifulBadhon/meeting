from django.db import models

# Create your models here.
class Meet(models.Model):
    subject = models.CharField(max_length=100)
    meetingWith = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    userId = models.IntegerField()
    done = models.BooleanField(default = False)
    summery = models.TextField(null=True,max_length=500)
    