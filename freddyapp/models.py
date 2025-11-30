# Tablas de la base de datos
from django.db import models

# Fiesta donde aparecen animatrónicos
class Party(models.Model):
    name = models.CharField(max_length=100)
    attendants = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.attendants} attendants)"

# Animatrónico del restaurante
class Animatronic(models.Model):
    ANIMAL_CHOICES = [
        ('BE', 'Bear'),
        ('CH', 'Chicken'),
        ('BU', 'Bunny'),
        ('FO', 'Fox'),
    ]

    name = models.CharField(max_length=50)
    animal = models.CharField(max_length=2, choices=ANIMAL_CHOICES)
    build_date = models.CharField(max_length=20)
    decommissioned = models.BooleanField(default=False)
    parties = models.ManyToManyField(Party, blank=True)

    def __str__(self):
        return self.name
