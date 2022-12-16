from django.db import models
from django.contrib.auth.models import User

class Parent(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= "parent")
    phone_number = models.IntegerField()

    @property
    def parent_name(self):
        return f'{self.user.first_name} {self.user.last_name}'