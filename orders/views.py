from django.forms import formset_factory
from django.shortcuts import render

from .forms import CommandeForm, ProduitForm, FournForm, PoForm
from .models import Commande, Produit, Fournisseur, Statut


def home(request):
    """
    A faire. Pour l'instant montre une page d'accueil de type Dashboard
    """
    return render(request, "dashboard.html", {})


def commande(request):
    """
    Liste des commandes.

    ToDo:
    -   Filter with status
    """
    queryset = Commande.objects.all()
    context = {
        'queryset': queryset
    }

    return render(request, "commande.html", context)


def add_commande(request):
    """
    Ajouter une commande.
    Lorsque le client arrive sur la page, le formulaire est présenté.
    Lorsque le formulaire est complété, une page montrant un message de succès est
    présentée.

    ToDo:
    -   Statut
    """

    ProduitFormSet = formset_factory(ProduitForm, extra=30)
    forms_prod = ProduitFormSet(request.POST or None)
    form_com = CommandeForm(request.POST or None)

    # 1st step
    context = {
        'title': 'Ajouter une commande',
        'form_com': form_com,
        'forms_prod': forms_prod,
    }

    # 2nd step
    if form_com.is_valid() and forms_prod.is_valid():
        statut = Statut.objects.filter(num_statut=1)[0]
        commande = form_com.save(commit=False)
        commande.statut = statut
        num_commande = commande.id  # Save numero de commande pour le montrer
        for form_prod in forms_prod:
            if all([x == '' for x in form_prod.cleaned_data.values()]):
                pass
            else:
                produit = form_prod.save(commit=False)
                produit.statut_produit = statut
                produit.commande = commande
                form_prod.save()
        commande.save()

        context = {
            'title': 'Commande ajouté!',
            'numero_commande': num_commande,
        }

    return render(request, "nouvelle_commande.html", context)


def po(request):
    """
    Page pour entrer les bons de commande.
    3 steps:
    1. Arrive sur la page et choisir le fournisseur
    2. Liste les produits qui doivent être commandés et cocher les produits qui le sont.
    3. Modifier le statut de ces produits, et montrer un message de succès.
    """
    fourn_form = FournForm(request.POST or None)

    # 1st step
    context = {
        'form': fourn_form
    }

    # 2nd step
    if fourn_form.is_valid():
        queryset = Produit.objects.all()
        po_form = PoForm()
        context = {
            'queryset': queryset,
            'po_form': po_form
        }

    # 3rd step

    return render(request, "po.html", context)
