from django.contrib import admin

from .models import Item, Project


objects = [
    Item,
    Project
    ]

admin.site.register(objects)
