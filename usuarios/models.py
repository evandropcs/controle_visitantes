from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UsuarioManager(BaseUserManager):

    def create_user(self, email, password=None):
        usuario = self.model(
            email=self.normalize_email(email)
        )

        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)

        usuario.save()

        return usuario

    def create_superuser(self, email, password):
        usuario = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password)

        usuario.save()

        return usuario


class Usuario(AbstractBaseUser, PermissionsMixin ):

    email = models.EmailField(
        verbose_name="E-mail do usuário",
        max_length=194,
        unique=True
    )

    # Verifica se está ativo
    is_active = models.BooleanField(
        verbose_name="Usuário está ativo",
        default=True
    )

    # Verifica se é dev
    is_staff = models.BooleanField(
        verbose_name="Usuário é da equipe de desenvolvimento",
        default=False,
    )

    # Verifica se é um super usuario
    is_superuser = models.BooleanField(
        verbose_name="Usuário é um super usuário",
        default=False
    )

    # Variavel que indica qual atributo da classe é usado como campo de autenticação
    USERNAME_FIELD = "email"

    # Sobreescreve a classe padrão na criação de modelos no django,
    # a object, para que ela utilize a classe UsuarioManager como padrão
    # Lembra de setar o settings do projeto, (criar a variavel AUTH_USER_MODEL = "
    objects = UsuarioManager()

    # Classe comum nos modelos do django, informa meta dados
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        db_table = "usuario"

    # Retorna o e-mail quando um usuário for criado
    def __str__(self):
        return self.email


