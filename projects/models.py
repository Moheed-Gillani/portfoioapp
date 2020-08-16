from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    technology=models.CharField(max_length=100)
    image=models.FileField()
    url=models.URLField( default='https://data-flair.training/blogs/django-crud-example/')
    uploaded=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
class Details(models.Model):

    detail=models.TextField()
    Project= models.OneToOneField('Project', related_name='Projects',on_delete=models.CASCADE)
    github=models.URLField(default='https://data-flair.training/blogs/django-crud-example/')
    def __str__(self):
        return self.Project.title
class Comment(models.Model):
    Details=models.ForeignKey('Details',on_delete=models.CASCADE)
    name=models.CharField(max_length=80,default='moheed')
    email=models.EmailField(default='a@gmail.com')
    Comment=models.TextField(default='good')
    created_on=models.DateTimeField(auto_now=True)
    active= models.BooleanField(default=False)
    class Meta:
        ordering = ['created_on']
    def __str__(self):
        return 'Comment {} by {}'.format(self.Comment, self.name)   
class Reviews(models.Model):
    name=models.CharField(max_length=80,default='moheed')
    email=models.EmailField(default='a@gmail.com')
    Review=models.TextField(default='good')
    created_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Review
    

