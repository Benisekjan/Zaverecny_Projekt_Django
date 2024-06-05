from django.contrib import admin
from .models import Dodavatele, Zakaznici, Doprava, PolozkyObjednavky, Vyrobek

admin.site.register(Dodavatele)
admin.site.register(Zakaznici)
admin.site.register(Doprava)
admin.site.register(PolozkyObjednavky)
admin.site.register(Vyrobek)