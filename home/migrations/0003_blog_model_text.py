# Generated by Django 5.1.1 on 2024-09-23 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_blog_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_model',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Text'),
        ),
    ]