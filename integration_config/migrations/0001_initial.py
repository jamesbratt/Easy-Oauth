# Generated by Django 2.1.2 on 2018-11-12 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IntegrationConf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('module_path', models.CharField(max_length=100)),
                ('oauth_class_name', models.CharField(max_length=100)),
                ('form_class_name', models.CharField(max_length=100)),
            ],
        ),
    ]
