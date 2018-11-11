"""Posts models"""

# Django

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Post model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    
    """Esto en caso de que se estén haciendo pruebas con la base de datos."""

    def __str__(self):
        """Returns Title and Username"""
        return '{} by @{}'.format(self.title, self.user.username)
