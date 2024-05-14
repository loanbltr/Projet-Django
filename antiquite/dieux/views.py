from django.shortcuts import render, HttpResponseRedirect
from .forms import DieuForm
from . import models

def ajout(request):
    if request.method == "POST":
        form = DieuForm(request)
        if form.is_valid():
            dieu = form.save()
            return render(request, "GodRead/affiche.html", {"dieu": dieu})

        else:
            return render(request, "GodRead/ajout.html", {"form": form})
    else:
        form = DieuForm()
        return render(request, "GodRead/ajout.html", {"form": form})

def traitement(request):
    dform = DieuForm(request.POST)
    if dform.is_valid():
        dieu = dform.save()
        return HttpResponseRedirect('/antiquite/')
    else:
        return render(request, 'GodRead/ajout.html', {'form': dform})

def index(request):
    return render(request, 'index.html')

def allGod(request):
    liste = list(models.Dieu.objects.all())
    return render(request, 'GodRead/allGod.html', {'liste': liste})

def affiche(request, id):
    dieu = models.Dieu.objects.get(pk=id)
    return render(request, 'GodRead/affiche.html', {'dieu': dieu})

def update(request, id):
    dieu = models.Dieu.objects.get(pk=id)
    form = DieuForm(dieu.dico())
    return render(request, 'GodRead/ajout.html', {'form': form, 'id': id})

def updatetraitement(request, id):
    dform = DieuForm(request.POST)
    if dform.is_valid():
        dieu = dform.save(commit=False)
        dieu.id = id
        dieu.save()
        return HttpResponseRedirect('/antiquite/allGod/')
    else:
        return render(request, 'GodRead/ajout.html', {'form': dform, 'id':id})

def delete(request, id):
    dieu = models.Dieu.objects.get(pk=id)
    dieu.delete()
    return HttpResponseRedirect('/antiquite/allGod/')