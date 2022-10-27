from django.db import models

# Create your models here.

class place(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='piture')
    price=models.IntegerField()
    desc=models.TextField()
    offer=models.BooleanField(default=False)






