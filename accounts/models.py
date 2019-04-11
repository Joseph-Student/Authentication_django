from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    """
    Aqui defines los campos que le quieras agregar al modelo y los metodos que necesites.
    """
    custom_field = models.CharField("Nombre del campo para los formularios", max_length=120, blank=True, null=True,
                                    help_text="Informacion sobre el campo.")
