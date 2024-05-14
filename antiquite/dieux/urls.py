from django.urls import path
from . import views, civilisation_views

urlpatterns = [
    path('', views.index),

    path('ajout/', views.ajout),
    path('allGod/', views.allGod),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/', views.affiche),
    path('update/<int:id>/', views.update),
    path('updatetraitement/<int:id>/', views.updatetraitement),
    path('delete/<int:id>/', views.delete),

    path('allCivilisation/', civilisation_views.civilisation_index),
    path('civilisationajout/', civilisation_views.civilisation_ajout),
    path('civilisationtraitement/', civilisation_views.civilisation_traitement),
    path('civilisationaffiche/<int:id>/', civilisation_views.civilisation_affiche),
    path('civilisationupdate/<int:id>/', civilisation_views.civilisation_update),
    path('civilisationupdatetraitement/<int:id>/', civilisation_views.civilisation_updatetraitement),
    path('civilisationdelete/<int:id>/', civilisation_views.civilisation_delete),
]