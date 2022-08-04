from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    name = models.fields.CharField(max_length=100)
    class Genre(models.TextChoices):
        ZOUGLOU = 'ZG'
        COUPE_DECALE= 'CD'
        SPOT= 'SP'
    
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.PositiveIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2022)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    #like_new = models.fields.BooleanField(default=False)
    def __str__(self):
        return f'{self.name}'


class Listing(models.Model):
    title = models.fields.CharField(max_length= 100)
    description =  models.fields.CharField(max_length= 100)
    class ListingType(models.TextChoices):
            RECORDS = 'R'#disques
            CLOTHINGS= 'C'# vetements
            POSTERS= 'P'
            MISCELLANEOUS ='MS' #Divers
    sold = models.fields.BooleanField(default=True)
    year = models.fields.PositiveIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2022)]
    )
    types = models.fields.CharField(choices=ListingType.choices, max_length=5)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title