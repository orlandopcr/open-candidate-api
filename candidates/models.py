from django.db import models


class PoliticalCoalition(models.Model):
    POLITICAL_SIDES = (
        ('IZQUIERDA', 'Izquierda'),
        ('CENTRO-IZQUIERDA', 'Centro izquierda'),
        ('CENTRO', 'Centro'),
        ('CENTRO-DERECHA', 'Centro derecha'),
        ('DERECHA', 'Derecha')
    )

    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    political_side = models.CharField(max_length=40, choices=POLITICAL_SIDES)


class Candidate(models.Model):
    STATES = (
        ('Active', 'Activo'),
        ('Inactive', 'Inactivo'),
    )

    name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    age = models.IntegerField(null=True)
    birth_date = models.DateField(null=True)
    state = models.CharField(max_length=30, choices=STATES)
    political_coalition = models.OneToOneField(PoliticalCoalition, on_delete=models.CASCADE)
