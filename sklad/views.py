from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Dodavatele, Zakaznici, Doprava, Objednavky, Vyrobek, PolozkyObjednavky

# Dodavatele Views
class DodavateleListView(ListView):
    model = Dodavatele
    template_name = 'dodavatele/dodavatele_list.html'
    context_object_name = 'dodavatele'

class DodavateleDetailView(DetailView):
    model = Dodavatele
    template_name = 'dodavatele/dodavatele_detail.html'
    context_object_name = 'dodavatel'


# Zakaznici Views
class ZakazniciListView(ListView):
    model = Zakaznici
    template_name = 'zakaznici/zakaznici_list.html'
    context_object_name = 'zakaznici'


class ZakazniciDetailView(DetailView):
    model = Zakaznici
    template_name = 'zakaznici/zakaznici_detail.html'
    context_object_name = 'zakaznik'


# Doprava Views
class DopravaListView(ListView):
    model = Doprava
    template_name = 'doprava/doprava_list.html'
    context_object_name = 'dopravci'

class DopravaDetailView(DetailView):
    model = Doprava
    template_name = 'doprava/doprava_detail.html'
    context_object_name = 'dopravce'

# Objednavky Views
class ObjednavkyListView(ListView):
    model = Objednavky
    template_name = 'objednavky/objednavky_list.html'
    context_object_name = 'objednavky'

class ObjednavkyDetailView(DetailView):
    model = Objednavky
    template_name = 'objednavky/objednavky_detail.html'
    context_object_name = 'objednavka'

# Vyrobek Views
class VyrobekListView(ListView):
    model = Vyrobek
    template_name = 'vyrobek/vyrobek_list.html'
    context_object_name = 'vyrobky'

class VyrobekDetailView(DetailView):
    model = Vyrobek
    template_name = 'vyrobek/vyrobek_detail.html'
    context_object_name = 'vyrobek'

# PolozkyObjednavky Views
class PolozkyObjednavkyListView(ListView):
    model = PolozkyObjednavky
    template_name = 'polozky_objednavky/polozky_objednavky_list.html'
    context_object_name = 'polozky'

class PolozkyObjednavkyDetailView(DetailView):
    model = PolozkyObjednavky
    template_name = 'polozky_objednavky/polozky_objednavky_detail.html'
    context_object_name = 'polozka'
