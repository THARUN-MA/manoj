from django.db import models

# Create your models here.
class userdetail(models.Model):
    email=models.CharField(max_length=264,unique=True)
    name=models.CharField(max_length=264)
    password=models.CharField(max_length=264)

    def __str__(self):
        return self.email

class userfiles(models.Model):
    files=models.FileField(upload_to="")
    aid=models.CharField(max_length=264)
    title=models.CharField(max_length=264)

    def __str__(self):
        return self.aid

class counter(models.Model):
    aid=models.CharField(max_length=264)

    def __str__(self):
        return self.aid
