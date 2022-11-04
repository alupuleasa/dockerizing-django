from django.db import models


class Item(models.Model):
    text = models.TextField(blank=False, null=False)
    date_posted = models.DateTimeField(auto_now_add=True, auto_now=True)
    print(date_posted)
