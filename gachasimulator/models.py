from django.db import models


class Character(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    RANK_CHOICE = (
        ('SSR', 'SSR'),
        ('SR', 'SR'),
        ('R', 'R')
    )
    rank = models.CharField(
        max_length=20,
        choices=RANK_CHOICE
    )
    game = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    image_path =  models.CharField(
        max_length=300,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name
