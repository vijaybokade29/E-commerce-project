# Generated by Django 5.0.1 on 2024-05-20 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='id',
        ),
        migrations.AddField(
            model_name='userdata',
            name='aboutme',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]