from django.forms import formset_factory
from django.shortcuts import render

from .forms import CommandeForm, ProduitForm, FournForm, PoForm
from .models import Commande, Produit, Fournisseur, Statut


# Create your views here.
def home(request):

    return render(request, "dashboard.html", {})


def add_commande(request):

    ProduitFormSet = formset_factory(ProduitForm, extra=30)
    form_prod = ProduitFormSet(request.POST or None)
    form_com = CommandeForm(request.POST or None)
    context = {
        'title': 'Ajouter une commande',
        'form_com': form_com,
        'formset': form_prod,
    }
    if form_com.is_valid() and form_prod.is_valid():
        statut = Statut.objects.filter(num_statut=1)[0]
        commande = form_com.save(commit=False)
        commande.statut = statut
        num_commande = commande.id
        # print form_com
        for form in form_prod:
            if all([x == '' for x in form.cleaned_data.values()]):
                pass
            else:
                produit = form.save(commit=False)
                produit.statut_produit = statut
                produit.commande = commande
                form.save()
        commande.save()

        context = {
            'title': 'Commande ajouté!',
            'numero_commande': num_commande,
        }

    return render(request, "nouvelle_commande.html", context)


def commande(request):
    queryset = Commande.objects.all()
    context = {
        'queryset': queryset
    }

    return render(request, "commande.html", context)


def po(request):
    fourn_form = FournForm(request.POST or None)
    context = {
        'form': fourn_form
    }

    if fourn_form.is_valid():
        queryset = Produit.objects.all()
        po_form = PoForm()
        context = {
            'queryset': queryset,
            'po_form': po_form
        }
        print(list(po_form.fields['produit'].choices))

    return render(request, "po.html", context)
