# Generated by Django 3.2.5 on 2021-08-05 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
    ]
