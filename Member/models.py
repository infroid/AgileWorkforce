from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Country(models.Model):
  code = models.CharField(max_length=10)
  name = models.CharField(max_length=250)

class State(models.Model):
  code = models.CharField(max_length=10)
  name = models.CharField(max_length=250)
  country = models.ForeignKey(Country, on_delete=models.CASCADE)

class City(models.Model):
  code = models.CharField(max_length=10)
  name = models.CharField(max_length=250)
  country = models.ForeignKey(Country, on_delete=models.CASCADE)
  state = models.ForeignKey(State, on_delete=models.CASCADE)

class Profile(models.Model):
  ROLE_CHOICES = (
    ('INT', 'Intern'),
    ('CNT', 'Contractor'),
    ('EMP', 'Employee'),
    ('OWN', 'Owner'),
  )

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  address = models.CharField(max_length=250)
  city = models.ForeignKey(City, on_delete=models.CASCADE)
  state = models.ForeignKey(State, on_delete=models.CASCADE)
  country = models.ForeignKey(Country, on_delete=models.CASCADE)
  date_of_birth = models.DateField(null=True, blank=True)
  role = models.CharField(choices=ROLE_CHOICES, max_length=3)
  earning = models.DecimalField(decimal_places=2)
  