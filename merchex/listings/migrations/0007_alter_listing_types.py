# Generated by Django 4.1 on 2022-08-04 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_remove_band_description_remove_band_sold_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='types',
            field=models.CharField(choices=[('R', 'Records'), ('C', 'Clothings'), ('P', 'Posters'), ('MS', 'Miscellaneous')], max_length=5),
        ),
    ]
