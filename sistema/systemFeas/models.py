from django.db import models

# Create your models here.
class bicicleta(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100,verbose_name='Título',null=True)
    imagen = models.ImageField(upload_to='imagenes/',verbose_name='Imagen',null=True)
    descripcion = models.TextField(verbose_name="Descripción",null=True)

#verbose_name es para darle un nombre visible al field
    
    def __str__(self):
        fila = 'Titulo: ' + self.titulo + ' - ' + 'Descripción: ' + self.descripcion
        return  fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()