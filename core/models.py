from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Link(models.Model):
    code = models.TextField(max_length=20, verbose_name="codigo")
    url = models.URLField("URL", unique=True)
    usuario = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name = "link"
        verbose_name_plural = "links"
        

    def __str__(self):
        return self.url

