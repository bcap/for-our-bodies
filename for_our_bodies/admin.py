import models

from django.contrib import admin

class InlineMeal(admin.StackedInline):
    model = models.MealEntry
    extra = 0

class EntryAdmin(admin.ModelAdmin):
    list_display = ('day', 'user', 'weight')
    inlines = [InlineMeal]

admin.site.register(models.User)
admin.site.register(models.Entry, EntryAdmin)