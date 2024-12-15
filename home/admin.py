from django.contrib import admin
from .models import service_model, blog_model
# Register your models here.
admin.site.register(service_model)
admin.site.register(blog_model)
