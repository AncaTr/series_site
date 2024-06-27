from django.contrib.auth.models import User
from django.db import models

class Gen(models.Model):
    nume = models.CharField(max_length=100)

    def __str__(self):
        return self.nume

class Tara(models.Model):
    nume = models.CharField(max_length=100)

    def __str__(self):
        return self.nume

class Serial(models.Model):
    titlu = models.CharField(max_length=200)
    descriere = models.TextField()
    genuri = models.ManyToManyField(Gen)
    tara = models.ForeignKey(Tara, on_delete=models.CASCADE)

    def __str__(self):
        return self.titlu

class Comentariu(models.Model):
    utilizator = models.ForeignKey(User, on_delete=models.CASCADE)
    serial = models.ForeignKey(Serial, on_delete=models.CASCADE)
    text = models.TextField()
    creat_la = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentariu de {self.utilizator.username} la {self.serial.titlu}'


class SeriesList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100000)

    def __str__(self):
        return self.name
