from django.db import models

class Characterfgo(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    RANK_CHOICE = (
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
    )
    rank_card = models.CharField(
        max_length=20,
        choices=RANK_CHOICE
    )
    TYPE_CHOICE = (
        ('servant', 'Servant'),
        ('craft_essense', 'Craft Essense'),
    )
    type_card = models.CharField(
        max_length=20,
        choices=TYPE_CHOICE
    )
    image_path =  models.CharField(
        max_length=300,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name

class FgoType(models.Model):
    None
