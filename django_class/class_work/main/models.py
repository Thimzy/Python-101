from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=255, )
    email = models.EmailField(unique=True)
    job_desc = models.TextField()
    age = models.IntegerField()
    img = models.ImageField()
    salary = models.FloatField()
    date_joined = models.DateTimeField()
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.email