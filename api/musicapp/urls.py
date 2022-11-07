
from django.urls import path
from .views import ListArtisteView


urlpatterns = [
    path('artistes/', ListArtisteView.as_view(), name="artiste-all")
]