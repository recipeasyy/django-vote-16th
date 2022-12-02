from django.db import models

# Create your models here.


class Team(models.Model):
    recipeasy = models.IntegerField(default=0)
    forgetmenot = models.IntegerField(default=0)
    prefolio = models.IntegerField(default=0)
    diametes = models.IntegerField(default=0)
    teample = models.IntegerField(default=0)

    def __str__(self):
        return 'Team'
