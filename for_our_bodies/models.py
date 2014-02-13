from django.db import models

class User(models.Model):
    name = models.CharField(max_length=60)


class Weight(models.Model):
    user = models.ForeignKey(User)
    weight = models.IntegerField(default=0)
    when = models.DateField(auto_now=True)
