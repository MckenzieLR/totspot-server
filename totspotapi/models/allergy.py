from django.db import models


class Allergy(models.Model):
    type = models.CharField(max_length=50)
