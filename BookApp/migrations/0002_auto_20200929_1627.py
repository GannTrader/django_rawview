# Generated by Django 3.1.1 on 2020-09-29 09:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='body',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
