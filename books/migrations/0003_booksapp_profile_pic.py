# Generated by Django 4.2.6 on 2023-11-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_booksapp_publisheddate'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksapp',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]