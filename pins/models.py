from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Pin(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    link = models.CharField(max_length=255)
    image_link = models.CharField(max_length=255)
    create_date = models.DateTimeField('date created', auto_now_add=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    caption = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return "Pin: %s" % self.title
