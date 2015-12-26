from django.contrib import admin

# Register your models here.

from .models import Commande
from .models import Produit
from .models import Fournisseur
from .models import Employe
from .models import Statut

admin.site.register(Commande)
admin.site.register(Produit)
admin.site.register(Fournisseur)
admin.site.register(Employe)
admin.site.register(Statut)
