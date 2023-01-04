from django.db import models

class DailyCheckIn(models.Model):
    provider = models.ForeignKey("Provider", on_delete= models.CASCADE, related_name= "provider_check_in")
    child = models.ForeignKey("Child", on_delete=models.CASCADE, related_name="child_check_in")
    content = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)
