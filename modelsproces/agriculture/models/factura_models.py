from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

class Factura(models.Model):
    numFact = models.TextField()
    descripcio = models.TextField()
    date = models.DateField(default=date.today)
    retencions = models.IntegerField(blank=True, null=True)
    impostos = models.FloatField(blank=True, null=True)
    preu_sense_impostos = models.FloatField(blank=True, null=True)


    def __unicode__(self):
        return u"%s" % self.name

    def __str__(self):
        return str(self.name)

    def obtain_address(self):
        return str(self.street) + '; ' + str(self.number) + '; ' + str(self.city)

    def get_absolute_url(self):

        return reverse('agriculture:factura_detail', kwargs={'pk': self.pk})