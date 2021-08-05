# Generated by Django 3.2.5 on 2021-08-05 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crmapi', '0002_alter_user_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry_Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('course_interest', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=250)),
                ('claimed_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userclaimedenquiries', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
