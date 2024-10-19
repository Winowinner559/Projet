from django.urls import path
from . import views  # Importer les vues de l'application

urlpatterns = [
    path('', views.index, name='index'),  # Affiche la vue index à la racine de l'URL
    path('login/', views.login_view, name='login'),
]
