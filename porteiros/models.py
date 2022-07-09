from django.db import models


# Classe padrão do django
class Porteiro(models.Model):

    # Tem uma relação de um para um
    usuario = models.OneToOneField(
        # Aplicativo e Classe que servirá de modelo para a criação do porteiro
        "usuarios.Usuario",
        verbose_name="Usuário",
        # Protege o registro do porteiro para que não seja excluido
        on_delete=models.PROTECT,
    )

    nome_completo = models.CharField(
        verbose_name="Nome completo",
        max_length=194,
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
    )

    telefone = models.CharField(
        verbose_name="Numero de contato",
        max_length=11,
    )

    data_nascimento = models.DateField(
        verbose_name="Data de nascimento",
        auto_now=False,
        auto_now_add=False,
    )

    class Meta:
        verbose_name = "Porteiro"
        verbose_name_plural = "Porteiros"
        db_table = "porteiro"

    def __str__(self):
        return self.nome_completo

