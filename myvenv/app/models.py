from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Nombre',
        help_text='Nombre del equipo'
    )

    user = models.ManyToManyField(
        User,
        verbose_name='Usuario',
        help_text='Usuarios que hacen parte del equipo'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'


class Project(models.Model):
    team = models.ForeignKey(
        Team,
        verbose_name='Equipo',
        on_delete=models.CASCADE,
        help_text='Equipo al que pertenece el proyecto'
    )

    name = models.CharField(
        max_length=200,
        verbose_name='nombre',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'


class UserHistory(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Título',
    )
    history_type = models.TextField(
        verbose_name='Tipo de historia',
    )

    description = models.TextField(
        verbose_name='descripción',
    )
    criteria_of_acceptance = models.TextField(
        verbose_name='criterio de aceptación',
    )
    interface_requirements = models.TextField(
        verbose_name='requerimientos de interfaz',
    )
    dependencies = models.TextField(
        verbose_name='dependencias',
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name='Proyecto',
        help_text='Proyecto al que pertenece la historia de usuario'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Historia de usuario'
        verbose_name_plural = 'Historia de usuarios'
