from django.db import models

# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to='media/')

    def __str__(self):
        return self.file.path