from django.db import models

# Create your models here.


class Candidate(models.Model):
    POSITION = (
        ('FE', 'FRONTEND'),
        ('BE', 'BACKEND')
    )

    name = models.CharField(max_length=20)
    position = models.CharField(choices=POSITION, max_length=2)
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}: {self.vote_count}'
