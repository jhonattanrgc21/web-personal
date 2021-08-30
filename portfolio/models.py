# Modelos de la app Portfolio
from django.db import models

class Project(models.Model):
    ''' Modelo de Proyectos '''

    # Aatributos
    title = models.CharField(
        max_length=200,
        verbose_name = 'Titulo'
    )

    description = models.TextField(verbose_name = 'Descripcion')
    image = models.ImageField(
        upload_to = 'media/projects',
        verbose_name = 'Imagen'
    )

    link = models.URLField(
        null=True,
        blank=True,
        verbose_name = 'Direccion web'
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ''' La clase Meta permite ordenar la lista de proyectos
            por fecha de creacion y traduce el nombre de la
            entidad de ingles a español en el dashboard '''
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']

    # Metodos
    def __str__(self):
        return self.title