from django import forms
from .models import Commande, Produit, Employe, Fournisseur


class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['nom_client', 'telephone', 'telephone2', 'emp_commande', 'note', 'ETA']


class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['quantite', 'produit', 'fournisseur', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2}),
        }


class FournForm(forms.Form):
    fournisseur = forms.ModelChoiceField(queryset=Fournisseur.objects.all(), empty_label=None)


class MyModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return ''


class PoForm(forms.Form):
    produit = MyModelMultipleChoiceField(queryset=Produit.objects.all(),
                                             widget=forms.CheckboxSelectMultiple)
