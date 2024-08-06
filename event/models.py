from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRunner(AbstractUser):
    pass


class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    event_type = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Result(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    runner = models.ForeignKey(UserRunner, on_delete=models.CASCADE)
    time = models.DateTimeField()
    position = models.IntegerField()

    def __str__(self):
        return f"{self.position} place {self.runner.last_name} {self.runner.first_name} {self.time}"


class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(UserRunner, on_delete=models.CASCADE)
    registration_date = models.DateTimeField()
    status = models.CharField(max_length=100, choices=[("Registered", "Registered"), ("Canceled", "Canceled")])

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"

    def cancel_registration(self):
        self.status = "Canceled"
        self.save()

    def is_active(self):
        return self.status == "Registered"
