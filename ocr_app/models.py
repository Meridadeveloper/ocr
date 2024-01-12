from django.db import models

# Create your models here.
class userprofile(models.Model):
    title = models.CharField(max_length=4)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=40)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    university = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.username
class studies(models.Model):
    user = models.OneToOneField(userprofile,on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    year = models.DateField() 
    def __str__(self):
        return self.user.username
    
class documents(models.Model):
    user = models.ForeignKey(userprofile,on_delete=models.CASCADE)
    document = models.FileField()
    likes = models.IntegerField(default=0)
    # comments = models.CharField(max_length=1000000,default='....')

    def __str__(self):

        return self.user.username
class comments(models.Model):
    user = models.ForeignKey(userprofile, on_delete=models.CASCADE)
    document = models.ForeignKey(documents, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user.username} - {self.document.id} - {self.created_at}'

class replies(models.Model):
    user = models.ForeignKey(userprofile, on_delete=models.CASCADE)
    comment = models.ForeignKey(comments, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.comment.id} - {self.created_at}'

class File(models.Model):
    file = models.FileField(upload_to='media/')
    def __str__(self):
        return self.file.path

