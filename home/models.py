from django.db import models

# Create your models here.
class service_model(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True, verbose_name='Title')
    text = models.TextField(blank=True, null=True, verbose_name='Text')
    img = models.FileField(upload_to='image/', blank=True, null=True)
    def __str__(self):
        return self.title
    

class blog_model(models.Model):
    title = models.TextField(blank=True, null=True, verbose_name='Title')
    text = models.TextField(blank=True, null=True, verbose_name='Text')
    tag = models.CharField(max_length=20, blank=True, null=True, verbose_name='Tag')
    image = models.FileField(upload_to='image/', blank=True, null=True)
    avatar = models.FileField(upload_to='image/', blank=True, null=True)
    user_name = models.CharField(max_length=20, blank=True, null=True, verbose_name='Username')
    date = models.DateField(verbose_name='Date')
    def __str__(self):
        return self.title
    