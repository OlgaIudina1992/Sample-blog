# Generated by Django 4.2.1 on 2023-06-03 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Please add a snippet', max_length=500),
        ),
    ]
