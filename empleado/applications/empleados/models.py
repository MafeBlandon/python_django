from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

class habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    
    class meta:
        verbose_name = 'Habilidad' #como quiero que se llame el modelo 
        verbose_name_plural = 'habilidades empleado'#cuando este en plurar le ponga un nombre
    
    def __str__(self):
        return str(self.id)+ '-' + self.habilidad
       

#Create your models here.
class Empleado(models.Model):
    #""" Modelo para la tabla empleado """

    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),

    )
    #contador administrador economista otro 
    first_name = models.CharField('Nombres',max_length=60)
    last_name = models.CharField('apellidos',max_length=60)
    full_name = models.CharField('Nombre Completo ',max_length=120, blank=True)#concatenacion de last_name y first_name
    job = models.CharField('Trabajo',max_length=1, choices= JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
   # avatar = models.ImageField(upload_to='empleados', blank=True, null=True)
    habilidades = models.ManyToManyField(habilidades)#realacionde muchos a muchos entre empleado y habilidades
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['first_name','last_name']
        


    def __str__(self):  
        return str(self.id) + '-' + self.first_name + '-' + self.last_name 
# Create your models here.
