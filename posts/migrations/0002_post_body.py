# Generated by Django 2.1.5 on 2019-01-13 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
