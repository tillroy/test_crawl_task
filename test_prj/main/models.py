from datetime import datetime


from django.db import models

# Create your models here.
# from django.db import models
from django.utils import timezone


class CurrencyСorrelation(models.Model):
    from_cur = models.CharField(max_length=10, null=False, blank=False)
    to_cur = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return "{}->{}".format(self.from_cur, self.to_cur)


class CurrencyValue(models.Model):
    correlation = models.ForeignKey(CurrencyСorrelation, on_delete=models.CASCADE)
    value = models.FloatField(max_length=10, null=False, blank=False)

    def __str__(self):
        return "{}->{}".format(self.correlation, self.value)