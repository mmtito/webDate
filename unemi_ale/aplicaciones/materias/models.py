from django.db import models
from aplicaciones.docente.models import Docente

# Create your models here.
class Cursos (models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    número_créditos = models.IntegerField()
    nivel = models.CharField(max_length=100)
    horas_clase_semana = models.IntegerField()
    jornada = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='curso/', blank=True, null=True)
    

    def __str__(self):
        return str(self.id) | ' - ' | self.nombre


    class Meta:
        db_table = 'cursos'
