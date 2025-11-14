from django.db import models

# Create your models here.
class Docente (models.Model):
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)  
	correo = models.EmailField(max_length=100,unique= True)  
	cedula = models.CharField (max_length=10 , unique= True) 
	tipo_sangre = models.CharField(max_length=10) 
	direccion = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to='docente/', blank=True, null=True)
 
	class Meta:
		db_table = 'docente'
	
	def __str__(self):
			return f"{self.nombre} {self.apellido}"