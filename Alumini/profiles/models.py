from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CollegeDetails(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    batch = models.IntegerField()

    class Meta:
        verbose_name = "College Detail"
        verbose_name_plural = "College Details"

    def __str__(self):
        return str(self.user)

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    facebook = models.URLField(max_length=100, blank=True, null=True)
    instagram = models.URLField(max_length=100, blank=True, null=True)
    linkedin = models.URLField(max_length=100, blank=True, null=True)
    github = models.URLField(max_length=100, blank=True, null=True)
    profilepic = models.ImageField(default='/profile_pics/default.png', upload_to='pictures/profile_pics', blank='true')

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return str(self.user)
