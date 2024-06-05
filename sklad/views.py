from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Dodavatele, Zakaznici, Doprava, Objednavky, Vyrobek, PolozkyObjednavky

# Dodavatele Views
class DodavateleListView(ListView):
    model = Dodavatele
    template_name = 'dodavatele_list.html'

class DodavateleDetailView(DetailView):
    model = Dodavatele
    template_name = 'dodavatele_detail.html'

# Zakaznici Views
class ZakazniciListView(ListView):
    model = Zakaznici
    template_name = 'zakaznici_list.html'

class ZakazniciDetailView(DetailView):
    model = Zakaznici
    template_name = 'zakaznici_detail.html'

# Doprava Views
class DopravaListView(ListView):
    model = Doprava
    template_name = 'doprava_list.html'

class DopravaDetailView(DetailView):
    model = Doprava
    template_name = 'doprava_detail.html'

# Objednavky Views
class ObjednavkyListView(ListView):
    model = Objednavky
    template_name = 'objednavky_list.html'

class ObjednavkyDetailView(DetailView):
    model = Objednavky
    template_name = 'objednavky_detail.html'

# Vyrobek Views
class VyrobekListView(ListView):
    model = Vyrobek
    template_name = 'vyrobek_list.html'

class VyrobekDetailView(DetailView):
    model = Vyrobek
    template_name = 'vyrobek_detail.html'

# PolozkyObjednavky Views
class PolozkyObjednavkyListView(ListView):
    model = PolozkyObjednavky
    template_name = 'polozky_objednavky_list.html'

class PolozkyObjednavkyDetailView(DetailView):
    model = PolozkyObjednavky
    template_name = 'polozky_objednavky_detail.html'
