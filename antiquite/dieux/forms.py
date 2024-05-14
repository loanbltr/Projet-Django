from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms

class DieuForm(ModelForm):
    class Meta:
        model = models.Dieu
        fields = ('nom', 'association', 'arme', 'histoire', 'civilisation')
        labels = {
            'nom': _('Nom'),
            'association': _('Association'),
            'arme': _('Arme'),
            'histoire': _('Histoire'),
            'civilisation': _('Civilisation'),
        }

class CivilisationForm(ModelForm):
    class Meta:
        model = models.civilisation
        fields = ('nom', 'desc')
        labels = {
            'nom' : _('Nom'),
            'desc' : _('Description'),
        }