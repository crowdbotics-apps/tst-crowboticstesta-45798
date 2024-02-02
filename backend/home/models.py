from django.conf import settings
from django.db import models


class Dwfe(models.Model):
    "Generated Model"
    sdv = models.BigIntegerField()
    wer = models.CharField(
        max_length=96,
    )
