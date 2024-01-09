from django.db import models
from app.forms import *

# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to='media/')

    def __str__(self):
        return self.file.path

