from django.db import models

# Create your models here.


class Office(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Employee(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=50, null=True)
    office = models.ForeignKey(Office, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Visitor(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField()
    visitee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    VISITOR_STATUS_CHOICES = [
        ('w', 'waiting for check-in'),
        ('i', 'in building'),
        ('c', 'checked_out')
    ]
