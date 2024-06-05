from django.db import models

class Dodavatele(models.Model):
    nazev_dodavatele= models.CharField(max_length=50, verbose_name='Nazev Dodavatele', help_text='Vložte název Dodavatele')
    email_dodavatele= models.CharField(max_length=50, unique=True, verbose_name='Email', help_text='Vložte email Dodavatele')
    telefon_dodavatele=  models.CharField(max_length=13, unique=True, verbose_name='Cislo', help_text='Vložte číslo Dodavatele')
    kontaktOs_dodavatele= models.CharField(max_length=50, verbose_name='Kontaktni Osoba', help_text='Vložte email Dodavatele')

    class Meta:
        verbose_name = 'Dodavatel'
        verbose_name_plural = 'Dodavatele'
        ordering = ['nazev_dodavatele']

    def __str__(self):
        return self.nazev_dodavatele


class Zakaznici(models.Model):
    jmeno_zakaznik = models.CharField(max_length=50, verbose_name='Jmeno zákazníka',help_text='Zadejte jméno ')
    prijmeni_zakaznik = models.CharField(max_length=50, verbose_name='Příjmení zákazníka',help_text='Zadejte příjmení')
    email_zakaznik = models.CharField(max_length=50, unique=True, verbose_name='Email zákazníka',help_text='Zadejte email')
    telefon_zakaznik = models.IntegerField(max_length=13, unique=True, verbose_name='Telefon zákazníka',help_text='Zadejte telefon')
    zeme_zakaznik = models.CharField(max_length=50,verbose_name='Země',help_text='Zadejte název Země')
    mesto_zakaznik = models.CharField(max_length=50,verbose_name='Město',help_text='Název Města')
    ulice_zakaznik = models.CharField(max_length=50,verbose_name='Ulice',help_text='Název Ulici')
    psc_zakaznik = models.IntegerField(max_length=6,verbose_name='Psč',help_text='Psč města')

    class Meta:
        db_table = 'zakaznici'
        ordering = ['prijmeni_zakaznik', 'jmeno_zakaznik']
        verbose_name = 'Zákazník'
        verbose_name_plural = 'Zákazníci'
        unique_together = (('jmeno_zakaznik', 'prijmeni_zakaznik', 'email_zakaznik', 'telefon_zakaznik'),)

    def __str__(self):
        return f"{self.jmeno_zakaznik} {self.prijmeni_zakaznik}"


class Doprava(models.Model):
    nazev_dopravce = models.CharField(max_length=50, verbose_name='Nazev dopravce',help_text='Zadejte název dopravce')
    adresa_dopravce = models.CharField(max_length=50, verbose_name='Adresa dopravce',help_text='Zadejte adresu dopravce')

    class Meta:
        db_table = 'doprava'
        ordering = ['nazev_dopravce']
        verbose_name = 'Dopravce'
        verbose_name_plural = 'Dopravci'

    def __str__(self):
        return self.nazev_dopravce


class Objednavky(models.Model):
    # Zde bylo odstraněno pole polozky_objenavky

    datum_objednavky = models.DateField(verbose_name='Datum objednávky', help_text='Zadejte datum objednávky')
    cena_objednavky = models.IntegerField(max_length=10, verbose_name='Cena objednávky',
                                          help_text='Zadejte cenu objednávky')
    datum_dopravy = models.DateField(verbose_name='Datum dopravy', help_text='Zadejte datum dopravy')
    doprava_id_dopravce = models.ForeignKey(Doprava, on_delete=models.CASCADE)
    zakaznici_id_zakaznik = models.ForeignKey(Zakaznici, on_delete=models.CASCADE)

    # PolozkyObjednavky jsou reprezentovány jako vazba mezi Objednavky a Vyrobek
    # To je realizováno pomocí ForeignKey k Objednavky a Vyrobek modelů.
    # Viz. definice PolozkyObjednavky níže.

    class Meta:
        db_table = 'objednavky'
        ordering = ['datum_objednavky']
        verbose_name = 'Objednávka'
        verbose_name_plural = 'Objednávky'

    def __str__(self):
        return f"Objednávka {self.id} - {self.datum_objednavky}"


class Vyrobek(models.Model):
    cena_vyrobku = models.IntegerField(
        verbose_name='Cena výrobku',
        help_text='Zadejte cenu výrobku'
    )
    nazev_vyrobku = models.CharField(
        max_length=50,
        verbose_name='Název výrobku',
        help_text='Zadejte název výrobku'
    )
    dodavatele_id_dodavatel = models.ForeignKey(
        'Dodavatele',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'vyrobky'
        ordering = ['nazev_vyrobku']
        verbose_name = 'Výrobek'
        verbose_name_plural = 'Výrobky'

    def __str__(self):
        return self.nazev_vyrobku


class PolozkyObjednavky(models.Model):
    objednavky_id_objednavky = models.ForeignKey(
        'Objednavky',
        on_delete=models.CASCADE
    )
    zasoby_id_vyrobek = models.ForeignKey(
        'Vyrobek',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'polozky_objednavky'
        unique_together = (('objednavky_id_objednavky', 'zasoby_id_vyrobek'),)
        verbose_name = 'Položka objednávky'
        verbose_name_plural = 'Položky objednávek'

    def __str__(self):
        return f"Položka objednávky {self.objednavky_id_objednavky.id} - {self.zasoby_id_vyrobek.nazev_vyrobku}"