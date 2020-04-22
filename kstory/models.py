from django.db import models

# Create your models here.


class MenuItem(models.Model):
    name = models.CharField(max_length=60)
    sequence = models.IntegerField()
    icon = models.CharField(max_length=20)
    url = models.CharField(max_length=140)
    parent = models.ForeignKey('self', null=True, related_name='child', on_delete=models.DO_NOTHING)
    description = models.TextField()
    active = models.BooleanField()

    objects = models.Manager()
