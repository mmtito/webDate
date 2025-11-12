from django.db import models
from aplicaciones.docente.models import Docente

# Create your models here.
class Cursos (models.Model):
    id_docente_fk = models.ForeignKey(Docente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, blank=False, null= False)
    número_créditos = models.IntegerField()
    nivel = models.CharField(max_length=100, blank=False, null= False)
    horas_clase_semana = models.IntegerField()
    jornada = models.CharField(max_length=100, blank=False, null= False)
    imagen = models.CharField(max_length=100, blank=False, null= False) 
