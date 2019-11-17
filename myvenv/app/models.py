from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser):
    username = models.CharField(
        max_length=200,
        verbose_name='nombre',
        default='name'
    )
    charge = models.CharField(
        max_length=200,
        verbose_name='Cargo',
        default='test'
    )

    salary = models.CharField(
        max_length=200,
        verbose_name='Salario',
    )

    income_date = models.DateField(
        verbose_name='Fecha de ingreso',
        auto_now=False
    )

    email = models.EmailField(
        verbose_name='email address',
        default='email@demo.co'
    )

    is_active = models.BooleanField(
        verbose_name='Estado',
        default=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


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

    manager_name = models.CharField(
        max_length=200,
        verbose_name='nombre del gerente',
        default='test'
    )

    manager_code = models.CharField(
        max_length=200,
        verbose_name='código del gerente',
        default='test'
    )

    planning_start_date = models.DateField(
        verbose_name='Fecha planeada de inicio',
        auto_now=False
    )

    planning_end_date = models.DateField(
        verbose_name='Fecha planeada de finalización',
        auto_now=False
    )

    real_start_date = models.DateField(
        verbose_name='Fecha real de inicio',
        auto_now=False
    )

    real_end_date = models.DateField(
        verbose_name='Fecha real de finalización',
        auto_now=False
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
