from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE


# Create your models here.

class Default(models.Model):
    name = models.CharField(max_length=256)
    reviewer = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    
    def __str__(self):
        return self.name[:50]