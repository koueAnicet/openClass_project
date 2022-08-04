from django.http import HttpResponse, request
from django.shortcuts import render
from listings.models import Band, Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect  # ajoutez cet import


def home(request):

    return HttpResponse('<h1>Bienvenue sur ma page!</h1>')

def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", {'bands': bands })

def band_detail(request, band_id):  # notez le paramètre id supplémentaire
    band = Band.objects.get(id=band_id)  # nous insérons cette ligne pour obtenir le Band avec cet id
    return render(request,
            'listings/band_detail.html',
            {'band': band}
    ) # nous mettons à jour cette ligne pour passer le groupe au gabarit

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, "listings/listing_list.html", {'listings': listings })

def listing_detail(request, listing_id):  # notez le paramètre id supplémentaire
    #print("la listing key:", listing_id)
    listing = Listing.objects.get(id=listing_id)  # nous insérons cette ligne pour obtenir le Band avec cet id
    return render(request,
            'listings/listing_detail.html',
            {'listing': listing}
    ) # nous mettons à jour cette ligne pour passer le groupe au gabarit
def listing_detail_annonce(request, listing_an_id):
    listing_annonce = Listing.objects.get(id=listing_an_id) 
    return render(request,
        'listings/listing_detail.html',
            {'listing_annonce': listing_annonce}
     )

def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
        return redirect("send-eamil")
        # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
        # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide : ', request.POST)

        form = ContactUsForm() # ceci doit être une requête GET, donc créer un formulaire vide
    return render(request,
        'listings/contact.html',
        {'form': form})  # passe ce formulaire au gabarit


def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def help(request):
    return HttpResponse("<h1>Bienvenue sur ma page d'aide!</h1>")