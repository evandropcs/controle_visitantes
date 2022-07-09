from django.db import models


class Visitantes(models.Model):

    nome_completo = models.CharField(
        verbose_name="Nome completo",
        max_length=194
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
    )

    data_nascimento = models.DateTimeField(
        verbose_name="Data de nascimento",
        auto_now=False,
        auto_now_add=False,
    )

    numero_casa = models.PositiveSmallIntegerField(
        verbose_name="Número da casa"
    )

    placa_veiculo = models.CharField(
        verbose_name="Placa do veículo",
        max_length=7,
        blank=True,
        null=True,
    )

    horario_chegada = models.DateTimeField(
        verbose_name="Horário de chegada na portaria",
        auto_now_add=True,
    )

    horario_saida = models.DateTimeField(
        verbose_name="Horário de saída do condominio",
        auto_now=False,
        blank=False,
        null=False,
    )

    horario_autorizacao_entrada = models.DateTimeField(
        verbose_name="Horário de autorização de entrada",
        auto_now=False,
        blank=False,
        null=False,
    )

    morador_responsavel = models.CharField(
        verbose_name="Nome do morador responsável por autorizar a entrada do visitante",
        max_length=256,
        blank=True,
    )
