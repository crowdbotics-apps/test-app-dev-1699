# Generated by Django 2.2.10 on 2020-02-21 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_testing'),
    ]

    operations = [
        migrations.AddField(
            model_name='testing',
            name='test',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
