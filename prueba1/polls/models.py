from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone


class Contacto(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    alias = models.CharField(max_length=15)
    email = models.EmailField(max_length=150)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_email()

    def get_email(self):
        return self.email





class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class prueba(models.Model):
    question = models.CharField(max_length=200)
