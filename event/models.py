from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Runner(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'),],
        null=True, blank=True
    )
    phone_number = models.CharField(max_length=15, null=True, blank=True)


class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('Running', 'Running'),
        ('Cycling', 'Cycling'),
        ('Swimming', 'Swimming'),
    ]

    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    event_type = models.CharField(max_length=100, choices=EVENT_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Result(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    runner = models.ForeignKey(Runner, on_delete=models.CASCADE)
    time = models.DateTimeField()
    position = models.IntegerField()

    def __str__(self):
        return f"{self.position} place {self.runner.last_name} {self.runner.first_name} {self.time}"


class EventRegistration(models.Model):
    DISTANCE_CHOICES_RUNNING = [
        (5, '5 km'),
        (10, '10 km'),
        (21, '21 km'),
        (42, '42 km'),
    ]
    DISTANCE_CHOICES_CYCLING = [
        (50, '50 km'),
        (100, '100 km'),
        (200, '200 km'),
    ]
    DISTANCE_CHOICES_SWIMMING = [
        (1, '1 km'),
        (2, '2 km'),
        (5, '5 km'),
        (10, '10 km'),
    ]

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(Runner, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    distance = models.IntegerField()
    status = models.CharField(max_length=100, choices=[("Registered", "Registered"), ("Canceled", "Canceled")])

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"

    def cancel_registration(self):
        self.status = "Canceled"
        self.save()

    def is_active(self):
        return self.status == "Registered"

    def get_distance_choices(self):
        if self.event.event_type == 'Running':
            return self.DISTANCE_CHOICES_RUNNING
        elif self.event.event_type == 'Cycling':
            return self.DISTANCE_CHOICES_CYCLING
        elif self.event.event_type == 'Swimming':
            return self.DISTANCE_CHOICES_SWIMMING
        else:
            return []

    def save(self, *args, **kwargs):
        if self.distance not in [choice[0] for choice in self.get_distance_choices()]:
            raise ValueError("Invalid distance for the event type")
        super().save(*args, **kwargs)
