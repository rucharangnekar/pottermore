from __future__ import unicode_literals
from django.db import models


class NewsDB(models.Model):
    rating = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    title = models.CharField(max_length=250, blank=True, null=True)
    background_color = models.CharField(max_length=50, blank=True, null=True)
    image = models.FileField(max_length=200, null=True, blank=True)
    date = models.CharField(max_length=200, null=True, blank=True)

    image1 = models.FileField(max_length=550, blank=True, null=True)
    caption1 = models.CharField(max_length=250, blank=True, null=True)

    main_text = models.CharField(max_length=500, blank=True, null=True)
    article1 = models.CharField(max_length=2000, blank=True, null=True)
    article2 = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.title + ' - ' + str(self.rating)


