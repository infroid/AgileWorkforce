from django.db import models
from django.contrib.auth.models import User


class Sprint(models.Model):
  STATUS_CHOICES = (
      ('WIP', 'Work in Progress'),
      ('PDR', 'Pending Review'),
      ('ACC', 'Accepted'),
      ('REJ', 'Rejected'),
  )

  user = models.ForeignKey(User, on_delete=models.PROTECT)
  start_date = models.DateField(null=True, blank=True)
  end_date = models.DateField(null=True, blank=True)
  status = models.CharField(choices=STATUS_CHOICES, max_length=3)

  def __str__(self):
    return f'{self.user.first_name} {self.user.last_name} -- {self.start_date}'


class Goal(models.Model):
  name = models.CharField(max_length=250)
  accomplished_date = models.DateField(null=True, blank=True)
  sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, related_name='goals')

  def __str__(self):
    return f'{self.sprint.__str__} -- {self.name}'