from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrador'
        GESTOR = 'GESTOR', 'Gestor'
        USUARIO = 'USUARIO', 'Usuario'
        VISITANTE = 'VISITANTE', 'Visitante'

    # CORREGIDO: 'role' en minúscula para que coincida con el admin
    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.VISITANTE,
        verbose_name="Rol del usuario"
    )

    # Grupos y permisos de Django
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='Groups this user belongs to.',
        related_name="custom_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_set",
        related_query_name="user",
    )

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"