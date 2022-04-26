from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_id = models.IntegerField()

class Item(models.Model):
    item_id = models.IntegerField()
    item_type = models.CharField(max_length=200)
    item_contents = models.TextField()