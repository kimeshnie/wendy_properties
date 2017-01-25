from django.db import models
from django.utils import timezone
from django.core.files.images import ImageFile
from django import forms
from django.utils.safestring import mark_safe
'''from django.contrib import admin'''

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

class Agents(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    cellphone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    model_pic = models.ImageField(upload_to='pic_folder/', default = 'images/None/no-img.jpg')

    def __unicode__(self):
        return self.first_name 


class Listings(models.Model):
    price = models.DecimalField(max_digits=9, decimal_places=2)
    bedrooms = models.DecimalField(max_digits=4, decimal_places=1)
    heading = models.CharField(max_length=240)
    desc = models.TextField()
    suburb = models.CharField(max_length=200)
    agent = models.ForeignKey(Agents,blank=True,null=True,)
    model_pic = models.ImageField(upload_to='pic_folder/', default = 'images/None/no-img.jpg')
    featured = models.BooleanField(null=False,)

    def __str__(self):
        return self.heading 

class Leads(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    desc = models.TextField()
    agent = models.ForeignKey(Agents,blank=True,null=True,)

    def __str__(self):
        lead_name = self.first_name + " " + self.last_name
        return lead_name
