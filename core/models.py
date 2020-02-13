from django.db import models
from django.contrib.auth.models import User

class LinkQuerySet(models.QuerySet):
    def from_user(self, user):
        return self.filter(user=user)


class Link(models.Model):
    code = models.TextField(max_length=20, unique=True, verbose_name="codigo")
    url = models.URLField( help_text=False)
    usuario = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    create = models.DateField(auto_now_add=True, verbose_name="Fecha de creacion")
    
    class Meta:
        verbose_name = "link"
        verbose_name_plural = "links"

    def __str__(self):
        return self.url

object=LinkQuerySet.as_manager()