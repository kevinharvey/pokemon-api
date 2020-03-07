from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    stage = models.CharField(max_length=10)
    evolves_from = models.ForeignKey('self', blank=True, null=True,
        on_delete=models.SET_NULL)
    hit_points = models.IntegerField()
    energy_type = models.CharField(max_length=10)


class Attack(models.Model):
    pokemon = models.ForeignKey(Pokemon, related_name='attacks', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    energy_required = models.IntegerField()
    damage = models.IntegerField()