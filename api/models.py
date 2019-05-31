from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):

    def create_user(self, email, name, password=None):
        """Cria usuário"""

        if not email:
            raise ValueError('Endereço de email é obrigatório.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Cria super usuário"""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Usado para obter um nome completo do usuário."""

        return self.name

    def get_short_name(self):
        """Usado para obter um nome abreviado do usuário."""

        return self.name

    def __str__(self):
        """Usado para converter o objeto em string"""

        return self.email


class ProfileFeedItem(models.Model):
    """Atualização de status do perfil."""

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Usado para converter o objeto em string"""

        return self.status_text

class DroidParts(models.Model):
    """Atualização de status do perfil."""

    description = models.CharField(max_length=255,help_text="Descrição do produto")
    address = models.CharField(max_length=255,help_text="Endereço completo")
    contact_information = models.CharField(max_length=255,help_text="Informações de contato")
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    # user = models.CharField(max_length=255, default=None)
    status = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def get_description(self):
        """Usado para obter a descrição da peça do Droid."""

        return self.description

    def get_address(self):
        """Usado para obter o endereço do anunciante da peça do Droid."""

        return self.address

    def get_contact_information(self):
        """Usado para obter a informação de contato do anunciante da peça do Droid."""

        return self.contact_information

    # def get_user(self):
    #     """Usado para obter o usuário logado."""

    #     return self.user

    def get_user_profile(self):
        """Usado para obter o usuário logado."""

        return self.user_profile

    def get_status(self):
        """Usado para obter o status da peça."""

        return self.status

    def get_created_on(self):

        return self.created_on
