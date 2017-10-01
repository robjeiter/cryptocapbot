from django.db import models

# Create your models here.

class User(models.Model):
    userid = models.CharField(max_length=26,unique=True)
    upper = models.IntegerField()
    lower = models.IntegerField()
    currency = models.CharField(max_length=3)
    lastmessagestatus = models.CharField(max_length=5)

    def __str__(self):
        return self.userid

