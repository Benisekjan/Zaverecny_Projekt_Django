from django.urls import path
from . import views

from django.views.generic import TemplateView

app_name = 'sklad'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('dodavatele/', views.DodavateleListView.as_view(), name='dodavatele_list'),
    path('dodavatele/<int:pk>/', views.DodavateleDetailView.as_view(), name='dodavatele_detail'),
    path('objednavky/<int:objednavka_id>/polozky_objednavky/', views.PolozkyObjednavky, name='polozky_objednavky'), #nevím jestli jede
    path('zakaznici', views.ZakazniciListView.as_view(), name='zakaznici_list'),
    path('zakaznici/<int:pk>/', views.ZakazniciDetailView.as_view(), name='zakaznici_detail'),
    path('doprava', views.DopravaListView.as_view(), name='doprava_list'),
    path('doprava/<int:pk>/', views.DopravaDetailView.as_view(), name='doprava_detail'),
    path('objednavky', views.ObjednavkyListView.as_view(), name='objednavky_list'),
    path('objednavky/<int:pk>/', views.ObjednavkyDetailView.as_view(), name='objednavky_detail'),
    path('vyrobek', views.VyrobekListView.as_view(), name='vyrobek_list'),
    path('vyrobek/<int:pk>/', views.VyrobekDetailView.as_view(), name='vyrobek_detail'),
    path('polozky_objednavky', views.PolozkyObjednavkyListView.as_view(), name='polozky_objednavky_list'),
    path('polozky_objednavky/<int:pk>/', views.PolozkyObjednavkyDetailView.as_view(), name='polozky_objednavky_detail'),
]
