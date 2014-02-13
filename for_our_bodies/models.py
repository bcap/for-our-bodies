from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    def __unicode__(self):
        return ', '.join(
            (': '.join((key, str(value))) for key, value in self.__dict__.iteritems() if not key.startswith('_'))
        )


class User(BaseModel):
    name = models.CharField(max_length=60)
    sleep_hours = models.IntegerField(default=8)


class Entry(BaseModel):
    user = models.ForeignKey(User)
    day = models.DateField()
    wakeup = models.DateTimeField()
    sleep = models.DateTimeField()
    weight = models.FloatField()

    class Meta(BaseModel.Meta):
        ordering = ['-day']
        verbose_name_plural = 'entries'


class MealEntry(BaseModel):
    entry = models.ForeignKey(Entry)
    meal = models.TextField()

    class Meta(BaseModel.Meta):
        verbose_name_plural = 'meals'