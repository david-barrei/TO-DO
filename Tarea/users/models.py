from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.


class users(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )

    email = models.EmailField(unique= True)
    full_name = models.CharField('Nombres',max_length=100)
    ocupation = models.CharField('Ocupacion',max_length=30,blank=False)
    genero = models.CharField(max_length=1,choices=GENDER_CHOICES, blank= True)
    date_birth = models.DateField('Fecha de nacimiento', blank=True,null=True)
    photo = models.ImageField(upload_to='imagenes',null=True, blank=True)

   
    USERNAME_FIELD = 'email'

    def get_short_name(self):
        return self.email
    
    def get_full_name(self):
        return self.full_name