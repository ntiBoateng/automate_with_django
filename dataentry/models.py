from django.db import models

# Create your models here.
class Student(models.Model):
    roll_number = models.CharField(max_length = 10)
    name = models.CharField(max_length = 20)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    
class Customer(models.Model):
    customer_name = models.CharField(max_length = 10)
    country = models.CharField(max_length = 30)

    def __str__(self) -> str:
        return self.customer_name