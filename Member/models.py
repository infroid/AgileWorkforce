from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
  code = models.CharField(max_length=10)
  name = models.CharField(max_length=250)

  def __str__(self):
    return self.name


class State(models.Model):
  code = models.CharField(max_length=10)
  name = models.CharField(max_length=250)
  country = models.ForeignKey(Country, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class City(models.Model):
  code = models.CharField(max_length=10)
  name = models.CharField(max_length=250)
  state = models.ForeignKey(State, on_delete=models.CASCADE)
  country = models.ForeignKey(Country, on_delete=models.CASCADE)

  def __str__(self):
    return self.name


class Job(models.Model):
  ROLE_CHOICES = (
      ('INT', 'Intern'),
      ('CNT', 'Contractor'),
      ('EMP', 'Employee'),
      ('OWN', 'Founder / Owner'),
  )

  role = models.CharField(choices=ROLE_CHOICES, max_length=3)
  profile = models.CharField(max_length=250)
  salary_per_sprint = models.DecimalField(max_digits=6, decimal_places=2)

  def __str__(self):
    return ' -- '.join([self.role,self.profile])
  
class Member(models.Model):
  STATUS_CHOICES = (
      ('NEW', 'New Member'),
      ('ACT', 'Active Member'),
      ('BLK', 'Blocked Member'),
  )

  user = models.OneToOneField(User, on_delete=models.PROTECT)
  city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='members')
  job = models.ForeignKey(Job, on_delete=models.PROTECT, related_name='members')
  amount_due = models.DecimalField(max_digits=10, decimal_places=2)
  amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
  status = models.CharField(choices=STATUS_CHOICES, max_length=3)

  def __str__(self):
    return ' -- '.join(self.user,self.job)