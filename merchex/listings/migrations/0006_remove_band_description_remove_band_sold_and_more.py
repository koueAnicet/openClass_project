# Generated by Django 4.1 on 2022-08-04 02:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_alter_band_genre_alter_band_types'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='description',
        ),
        migrations.RemoveField(
            model_name='band',
            name='sold',
        ),
        migrations.RemoveField(
            model_name='band',
            name='types',
        ),
        migrations.AlterField(
            model_name='band',
            name='year_formed',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2022)]),
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('sold', models.BooleanField(default=True)),
                ('year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2022)])),
                ('types', models.CharField(choices=[('RC', 'Records'), ('CL', 'Clothings'), ('PS', 'Posters'), ('Ma', 'Miscellaneous')], max_length=5)),
                ('band', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.band')),
            ],
        ),
    ]
