from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Dodavatele, Zakaznici, Doprava, Objednavky, Vyrobek, PolozkyObjednavky

# Dodavatele Views
class DodavateleListView(ListView):
    model = Dodavatele
    template_name = 'dodavatele/dodavatele_list.html'

class DodavateleDetailView(DetailView):
    model = Dodavatele
    template_name = 'dodavatele/dodavatele_detail.html'

# Zakaznici Views
class ZakazniciListView(ListView):
    model = Zakaznici
    template_name = 'zakaznici/zakaznici_list.html'

class ZakazniciDetailView(DetailView):
    model = Zakaznici
    template_name = 'zakaznici/zakaznici_detail.html'

# Doprava Views
class DopravaListView(ListView):
    model = Doprava
    template_name = 'doprava/doprava_list.html'

class DopravaDetailView(DetailView):
    model = Doprava
    template_name = 'doprava/doprava_detail.html'

# Objednavky Views
class ObjednavkyListView(ListView):
    model = Objednavky
    template_name = 'objednavky/objednavky_list.html'

class ObjednavkyDetailView(DetailView):
    model = Objednavky
    template_name = 'objednavky/objednavky_detail.html'

# Vyrobek Views
class VyrobekListView(ListView):
    model = Vyrobek
    template_name = 'vyrobek/vyrobek_list.html'

class VyrobekDetailView(DetailView):
    model = Vyrobek
    template_name = 'vyrobek/vyrobek_detail.html'

# PolozkyObjednavky Views
class PolozkyObjednavkyListView(ListView):
    model = PolozkyObjednavky
    template_name = 'polozky_objednavky/polozky_objednavky_list.html'

class PolozkyObjednavkyDetailView(DetailView):
    model = PolozkyObjednavky
    template_name = 'polozky_objednavky/polozky_objednavky_detail.html'
