from django.db import models

# Create your models here.


class BackEnd(models.Model):
    hyunyoung = models.IntegerField(default=0)
    junyeol = models.IntegerField(default=0)
    suhyun = models.IntegerField(default=0)
    hyejin = models.IntegerField(default=0)
    seunghee = models.IntegerField(default=0)
    sanghoon = models.IntegerField(default=0)
    junghyun = models.IntegerField(default=0)
    suah = models.IntegerField(default=0)
    jiahn = models.IntegerField(default=0)

    def __str__(self):
        return 'BackEnd'


class FrontEnd(models.Model):
    hanbi = models.IntegerField(default=0)
    hyunyoung = models.IntegerField(default=0)
    nayeon = models.IntegerField(default=0)
    seonyoung = models.IntegerField(default=0)
    chaeyeon = models.IntegerField(default=0)
    jieun = models.IntegerField(default=0)
    seonho = models.IntegerField(default=0)
    chaeri = models.IntegerField(default=0)
    youngjun = models.IntegerField(default=0)

    def __str__(self):
        return 'FrontEnd'
