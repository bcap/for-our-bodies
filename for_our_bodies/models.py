from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    def __repr__(self):
        return '<{}: {{{}}}>'.format(self.__class__.__name__, ', '.join(
            (': '.join((repr(key), repr(value))) for key, value in self.__dict__.iteritems() if not key.startswith('_'))
        ))


class User(BaseModel):
    name = models.CharField(max_length=60)
    sleep_hours = models.IntegerField(default=8)

    def __unicode__(self):
        return unicode(self.name)

    def entries(self):
        return self.entry_set.order_by('day')


class Entry(BaseModel):
    user = models.ForeignKey(User)
    day = models.DateField()
    wakeup = models.DateTimeField()
    sleep = models.DateTimeField()
    weight = models.FloatField()

    def __unicode__(self):
        return u'{} with {}kg at {}'.format(unicode(self.user), self.weight, self.day)

    class Meta(BaseModel.Meta):
        ordering = ['-day']
        verbose_name_plural = 'entries'


class MealEntry(BaseModel):
    entry = models.ForeignKey(Entry)
    meal = models.TextField()

    class Meta(BaseModel.Meta):
        verbose_name_plural = 'meals'