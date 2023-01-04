from django.db import models

class Announcement(models.Model):
    provider = models.ForeignKey("Provider", on_delete=models.CASCADE, related_name="provider_name")
    content = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)

    