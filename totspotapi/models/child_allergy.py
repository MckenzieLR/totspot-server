from django.db import models


class ChildAllergy(models.Model):
    child = models.ForeignKey("Child", on_delete=models.CASCADE, related_name="child_with_allergies")
    allergy = models.ForeignKey("Allergy", on_delete=models.CASCADE, related_name="child_allergy")