import email
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Therapy(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Therapy"


class Blog(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    link = models.CharField(max_length=100, default='')
    
    def __str__(self):
         return self.name + ' ' + self.description

    
    class Meta:
         verbose_name_plural = "Blog"

class Meditation(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    
    def __str__(self):
         return self.name + ' ' + self.link

    
    class Meta:
         verbose_name_plural = "Meditation"

class Rec(models.Model):
    recChoices = [
      ('song', 'song'),
      ('movie', 'movie'),
      ('tvShow', 'tvShow'),
      ('podcast', 'podcast'),
      ('book', 'book'),
   ]
    choices = models.CharField(choices=recChoices,null=True,blank=True,max_length=10)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    genre = models.CharField(max_length=100 , default= '')
    platform = models.CharField(max_length=100)
    link = models.CharField(max_length= 100, default='')
    
    def __str__(self):
         return self.name + ' ' + self.link

    class Meta:
         verbose_name_plural = "Recommendations"


class Profile(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name_plural = "Profile"


class Journaling(models.Model):
    cmpname = models.CharField(max_length=100,null=True, blank=True)
    position = models.CharField(max_length=100,null=True, blank=True)
    shortdescription = models.CharField(max_length=100,null=True, blank=True)
    updatedat = models.DateTimeField(auto_now=True)
    createdat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cmpname + ' ' + self.position
    
    class Meta:
        verbose_name_plural = "Journaling"


# class Timetable(models.Model):
#     edchoices = [
#         ('jr','junior'),
#         ('sr','senior'),
#         ('gr','graduate'),
#     ]
#     schname = models.CharField(max_length=100,null=True, blank=True)
#     hist = models.CharField(choices=edchoices,null=True,blank=True,max_length=10,default="junior")
#     position = models.CharField(max_length=100,null=True, blank=True)
#     shortdescription = models.CharField(max_length=100,null=True, blank=True)
#     updatedat = models.DateTimeField(auto_now=True)
#     createdat = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.schname + ' ' + self.hist

    
#     class Meta:
#         verbose_name_plural = "Education"