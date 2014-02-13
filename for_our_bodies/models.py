from django.db import models


class str_trait(object):
    def __unicode__(self):
        return ', '.join(
            (': '.join((key, str(value))) for key, value in self.__dict__.iteritems() if not key.startswith('_'))
        )


class User(models.Model, str_trait):
    name = models.CharField(max_length=60)
    sleep_hours = models.IntegerField(default=8)


class Entry(models.Model, str_trait):
    user = models.ForeignKey(User)
    day = models.DateField()
    wakeup = models.DateTimeField()
    sleep = models.DateTimeField()
    weight = models.FloatField()
    food = models.TextField()