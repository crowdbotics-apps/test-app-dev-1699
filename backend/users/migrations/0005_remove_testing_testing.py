# Generated by Django 2.2.10 on 2020-02-21 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_testing_test"),
    ]

    operations = [
        migrations.RemoveField(model_name="testing", name="testing",),
    ]
