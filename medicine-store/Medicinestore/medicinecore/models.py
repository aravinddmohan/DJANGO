from django.db import models
from django.contrib.auth.models import User

class Medicine(models.Model):
    name=models.CharField(max_length=100)
    stock=models.PositiveIntegerField()
    added_time=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name