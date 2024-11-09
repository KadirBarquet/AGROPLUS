from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=10, blank=True, help_text="Número de teléfono del usuario.")
    address = models.CharField(max_length=255, blank=True, help_text="Dirección del usuario.")
    date_of_birth = models.DateField(null=True, blank=True, help_text="Fecha de nacimiento del usuario.")
    gender = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], blank=True, help_text="Género del usuario.")
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    groups = models.ManyToManyField(Group, related_name='security_user_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='security_user_set', blank=True)