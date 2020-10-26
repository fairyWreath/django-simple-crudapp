from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Character(models.Model):
    firstName = models.CharField("First name", max_length=225, blank = True, null = True)
    lastName = models.CharField("Last name", max_length=255, blank = True, null = True)
    origin = models.CharField("Origin", max_length=255, blank = True, null = True)
    description = models.TextField(blank=True, null=True)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    rating = models.FloatField("Rating", validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ], null=True, blank=True)
    
    points = models.FloatField("Points", validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ], null=True, blank=True)
    
    createdAt = models.DateTimeField("Created At", auto_now_add=True)   # add auto now true

    STATUS_CHOICES = (
        ('AL', 'Alive'),
        ('DC', 'Deceased'),
        ('UK', 'Unknown')
    )

    status = models.CharField("Status", max_length=255, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.firstName}, {self.lastName}'