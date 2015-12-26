from django.db import models


# Create your models here.
class Statut(models.Model):
    num_statut = models.SmallIntegerField('numéro du statut')
    nom_statut = models.CharField('Statut', max_length=20)

    def __str__(self):
        return '{} - {}'.format(self.num_statut, self.nom_statut)


class Fournisseur(models.Model):
    nom = models.CharField(max_length=50)
    phone = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.nom


class Employe(models.Model):
    nom = models.CharField(max_length=40)
    nom_complet = models.CharField(max_length=100, blank=True, null=True)
    short = models.CharField(max_length=3)

    def __str__(self):
        return self.nom


class Commande(models.Model):
    # num = models.CharField(max_length=10, primary_key=True)

    # Client
    nom_client = models.CharField(
        'nom du client', max_length=120,
        error_messages={'required': 'Champ requis'})
    telephone = models.CharField(
        'téléphone', max_length=40,
        error_messages={'required': 'Champ requis'})
    telephone2 = models.CharField(
        'téléphone extra', max_length=40, blank=True, null=True)

    # Commande
    statut = models.ForeignKey(Statut, related_name='status')
    # statut = models.CharField(max_length=10)
    note = models.TextField(blank=True, null=True)

    emp_commande = models.ForeignKey(Employe,
                                     verbose_name='Employé',
                                     related_name='emp_commande')
    emp_po = models.ForeignKey(Employe,
                               verbose_name='Employé',
                               related_name='emp_po',
                               blank=True, null=True)
    emp_appel = models.ForeignKey(Employe,
                                  verbose_name='Employé',
                                  related_name='emp_appel',
                                  blank=True, null=True)
    emp_complete = models.ForeignKey(Employe,
                                     verbose_name='Employé',
                                     related_name='emp_complete',
                                     blank=True, null=True)

    ts_commande = models.DateTimeField(auto_now_add=True, auto_now=False)
    ts_po = models.DateTimeField(blank=True, null=True)
    ts_appel = models.DateTimeField(blank=True, null=True)
    ts_complete = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    ETA = models.DateField(blank=True, null=True)


class Produit(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.CharField(max_length=500)
    quantite = models.SmallIntegerField('Quantité')
    description = models.TextField(blank=True, null=True)
    statut_produit = models.ForeignKey(Statut)
    # Fournisseur
    fournisseur = models.ForeignKey(Fournisseur, related_name='fournisseur')
    purchase_order = models.CharField(max_length=40)

