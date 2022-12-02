from django.db import models

# Create your models here.

PART_CHOICE = (
    ('Backend', 'Backend'),
    ('Frontend', 'Frontend'),
    ('Design', 'Design'),
    ('PM', 'PM')
)


TEAM_CHOICE = (
    ('Recipeasy', 'Recipeasy'),
    ('Forgetmenot', 'Forgetmenot'),
    ('Prefolio', 'Prefolio'),
    ('Diametes', 'Diametes'),
    ('Teample', 'Teample')
)


class User(models.Model):
    user_id = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=20, unique=True)
    name = models.CharField(max_length=20)
    part = models.CharField(max_length=20, choices=PART_CHOICE)
    team = models.CharField(max_length=20, choices=TEAM_CHOICE)
    demoday = models.BooleanField(default=False)
    part = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} ({self.part})'
