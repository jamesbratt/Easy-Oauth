# Generated by Django 2.1.2 on 2018-10-24 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='callbackUrl',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
