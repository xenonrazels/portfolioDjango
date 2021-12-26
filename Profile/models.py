from django.db import models
from django.db.models.enums import Choices

# Create your models here.
class Experience(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    experience_yrs_start=models.DateField(blank=True)
    experience_yrs_start=models.DateField(blank=True)

    def __str__(self):
        return self.title


class Introduction(models.Model):
    CHOICES=(('Male',"M"),("Female","F"))
    name=models.CharField(max_length=50)
    email=models.EmailField( max_length=254)
    profilePic=models.ImageField(upload_to='Portfolio')
    date=models.DateField()
    Gender=models.CharField(choices=CHOICES, max_length=50)
    contact_num=models.BigIntegerField()
    Nationality=models.CharField(max_length=30)
    resume=models.FileField(upload_to='Portfolio/pdf')
    Resume_url=models.URLField(blank=True)
    linked_url=models.URLField(blank=True)
    fb_url=models.URLField(blank=True)
    insta_url=models.URLField(blank=True)
    description=models.TextField()
    experience=models.ForeignKey('Experience',blank=True,on_delete=models.RESTRICT)

    def __str__(self):
        return self.name 


class Projects(models.Model):
    title=models.CharField(max_length=100)
    language_used=models.CharField(max_length=50)
    description=models.TextField()
    Project_url=models.URLField(blank=True)
    live_url=models.URLField(blank=True)
    Project_image=models.ImageField(upload_to='Project/Image')
    def __str__(self):
        return self.title


