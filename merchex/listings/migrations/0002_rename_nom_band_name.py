# Generated by Django 4.1 on 2022-08-03 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='band',
            old_name='nom',
            new_name='name',
        ),
    ]
