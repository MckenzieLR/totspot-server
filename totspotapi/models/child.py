from django.db import models

class Child(models.Model):
    parent = models.ForeignKey("Parent", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    medications = models.CharField(max_length=100)
    age = models.IntegerField()
    details = models.CharField(max_length=500)
    allergies = models.ManyToManyField("Allergy", blank=True, through='ChildAllergy', related_name='allergy')
   
    @property
    def allergy_type(self):
        return f'{self.allergies.type}'