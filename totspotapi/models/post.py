from django.db import models

class Post(models.Model):
    parent = models.ForeignKey("Parent", on_delete= models.CASCADE, related_name= "post_parent")
    content = models.CharField(max_length=512)
    date = models.DateField(auto_now_add=True)
