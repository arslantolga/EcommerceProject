from django.db import models

# Create your models here.

class buyer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    def __str__(self):
        return f"""
        Name : {self.name}
        Email : {self.email}
        Passowrd : {self.password}
        Address : {self.address}
        City : {self.city}
        State : {self.state}
        """
    
    
