from django.shortcuts import render, HttpResponseRedirect
from .forms import CivilisationForm
from . import models

# Create your views here.
def civilisation_index(request):
    liste = list(models.civilisation.objects.all())
    return render(request,"CivilisationRead/allCivilisation.html",{"liste" : liste})

def civilisation_ajout(request):
    if request.method == "POST":
        form = CivilisationForm(request)
        if form.is_valid():
            civilisation = form.save()
            return render(request, "CivilisationRead/affiche.html", {"civilisation": civilisation})

        else:
            return render(request, "CivilisationRead/ajout.html", {"form": form})
    else:
        form = CivilisationForm()
        return render(request, "CivilisationRead/ajout.html", {"form": form})


def civilisation_traitement(request):
    cform = CivilisationForm(request.POST)
    if cform.is_valid():
        civilisation = cform.save()
        return HttpResponseRedirect("/antiquite/")
    else:
        return render(request, "CivilisationRead/ajout.html", {"form": cform})

def civilisation_affiche(request, id):
    civilisation = models.civilisation.objects.get(pk=id)
    return render(request, "CivilisationRead/affiche.html", {"civilisation": civilisation})

def civilisation_update(request, id):
    liste = models.civilisation.objects.get(pk=id)
    form = CivilisationForm(liste.civilisation())
    return render(request, "CivilisationRead/ajout.html",{"form":form, "id": id})

def civilisation_updatetraitement(request, id):
    cform = CivilisationForm(request.POST)
    if cform.is_valid():
        civilisation = cform.save(commit = False)
        civilisation.id = id
        civilisation.save()
        return HttpResponseRedirect("/antiquite/")
    else:
        return render(request, "CivilisationRead/ajout.html", {"form": cform, "id":id})

def civilisation_delete(request, id):
    civilisation = models.civilisation.objects.get(pk=id)
    civilisation.delete()
    return HttpResponseRedirect("/antiquite/allCivilisation/")