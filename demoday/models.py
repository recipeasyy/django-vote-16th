from django.db import models

# Create your models here.


class Team(models.Model):

    CHOICES = (
        ('RECIPEASY', 'RECIPEASY'),
        ('TEAMPLE', 'TEAMPLE'),
        ('FORGET_ME_NOT', 'FORGET_ME_NOT'),
        ('PREFOLIO', 'PREFOLIO'),
        ('DIAMETES', 'DIAMETES')
    )

    team_name = models.CharField(choices=CHOICES, max_length=20)

    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.team_name


