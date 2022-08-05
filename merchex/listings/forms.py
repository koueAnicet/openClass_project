from django import forms
from listings.models import Band, Listing

class ContactUsForm(forms.Form):

    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

#le modelForm use le model pour lequel nous voulons créer une vue
class BandForm(forms.ModelForm):
    class Meta:
        model = Band #qui spécifie le modèle pour lequel ce formulaire sera utilisé
        #fields = '__all__' #les champs de ce modèle à inclure dans ce formulaire (ici tous)
        #exclu des champs d'un modelform
        exclude = ('active', 'official_homepage')  # ajoutez cette ligne

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'