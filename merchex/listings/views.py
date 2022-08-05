from django.http import HttpResponse, request,HttpResponseRedirect 
from django.urls import reverse
from django.shortcuts import render
from listings.models import Band, Listing
from listings.forms import BandForm, ContactUsForm, ListingForm
from django.core.mail import send_mail
from django.shortcuts import redirect # ajoutez cet import


def home(request):

    return HttpResponse('<h1>Bienvenue sur ma page!</h1>')

def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", {'bands': bands })

def band_detail(request, band_id): 
    # notez le paramètre id supplémentaire
    band = Band.objects.get(id=band_id)  # nous insérons cette ligne pour obtenir le Band avec cet id
    return render(request,
            'listings/band_detail.html',
            {'band': band}
    ) # nous mettons à jour cette ligne pour passer le groupe au gabarit
def band_create(request):
  
    if request.method == 'POST':
        form = BandForm(request.POST)
        
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            """ redirige vers la page de détail du groupe que nous venons de créer
                nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            """
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request,
            'listings/band_create.html',
            { 'form': form}
    )

def band_update(request, id):
    band= Band.objects.get(id=id)
    # on pré-remplir le formulaire avec un groupe existant ,par largument d'instance
    #form = BandForm(instance=band)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            band = form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
    else:
        # on pré-remplir le formulaire avec un groupe existant ,par largument d'instance
        form = BandForm(instance=band)
    return render(request,
                'listings/band_update.html',
                {'form': form}
    )

def band_delete(request, id):
    band= Band.objects.get(id=id)
    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('band-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement
    return render(request,
            'listings/band_delete.html',
            {'band': band})
            
def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        #validation
        if form.is_valid():
            #enregistrement
            listing = form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm()
    return  render(request,
            'listings/listing_create.html',
            { 'form': form})

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