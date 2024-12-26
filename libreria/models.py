from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre=models.CharField('Nombre', max_length = 100, null = False, blank = False)
    nacionalidad=models.CharField('Nacionalidad', max_length = 100, null = False, blank = False)
    edad=models.IntegerField('Edad', null = False, blank = False)
    fecha_na=models.DateField('Fecha de nacimiento', null = False, blank = False)
    
    class Meta:
        db_table = "autores"
    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField('Titulo', max_length = 50, null = False, blank = False)
    autor=models.ForeignKey(Autor,on_delete=models.CASCADE)
    genero=models.CharField('Genero', max_length = 50,null = False, blank = False)
    sinopsis=models.TextField('Sinopsis', null = False, blank = False)
    fecha_pu=models.DateField('Fecha de publicacion', null = False, blank = False)
    
    class Meta:
        db_table = "libros"
    def __str__(self):
        return self.titulo
