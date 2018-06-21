from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse

# Create your models here.

class Author_bio(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    bio=models.TextField(max_length=1000)
    Photo=models.ImageField(upload_to='uploads',null=True)

    def __str__(self):
        return str(self.user)


    def get_absolute_url(self):

        return reverse("blogger-details",args=[str(self.id)]) 

class blog(models.Model):

    Author=models.ForeignKey(Author_bio,on_delete=models.CASCADE)
    Title=models.CharField(max_length=500,help_text="Enter Blog Title")
    Description=models.TextField(max_length=10000,help_text="Enter Blog",null=True,blank=True)
    Date=models.DateField(default=date.today())
    

    class Meta:
        ordering = ["-Date"]


    def __str__(self):

        return self.Title

    def get_absolute_url(self):

        return reverse("blog-details",args=[str(self.id)])

class Comments(models.Model):

    Comment=models.TextField(max_length=500,help_text="Enter Comments")
    blog=models.ForeignKey(blog,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.SET_DEFAULT,default="no-user")

    def __str__(self):
        return str(self.id)

   