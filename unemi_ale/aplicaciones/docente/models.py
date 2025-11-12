from django.db import models

# Create your models here.
class Docente (models.Model):
	nombre = models.CharField(max_length=100, blank=False, null= False ), 
	apellido = models,models.CharField(_max_length=100, blank= False, null= False)  
	correo = models.EmailField(max_length=100,unique= True)  
	cédula = models.CharField (max_length=10 , unique= True) 
	tipo_sangre = models.CharField(max_length=10, blank= False, null= False), 
	dirección = models.CharField(max_length=100, blank= False, null= False), 
	imagen = models.CharField(max_length=100, blank= False, null= False)
