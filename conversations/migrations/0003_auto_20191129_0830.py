# Generated by Django 2.2.5 on 2019-11-28 23:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0002_auto_20191129_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='conversations', to=settings.AUTH_USER_MODEL),
        ),
    ]
