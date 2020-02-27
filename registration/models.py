from django.db import models
from django.contrib.auth.models import User


# Create your models here.
def custom_upload_to(instance, filename):
    """ Method for upload to. This method search and delete old image, then redirect to profiles/filename"""
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename
    #filter objets whith pk and delete old image object, then redirect to user profiles/filename 


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
