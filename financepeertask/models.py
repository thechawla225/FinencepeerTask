from django.db import models


class Details(models.Model):

    userId = models.IntegerField()
    id1 = models.IntegerField()
    title = models.CharField(max_length=1000)
    body = models.CharField(max_length=1000)

    def __set__(self):
        return self.userId
