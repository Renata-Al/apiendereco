from django.db import models
from django.core.validators import RegexValidator

class Endereco(models.Model):
    # Campos OBRIGATÓRIOS
    cep = models.CharField(
        max_length=9,
        verbose_name="CEP",
        validators=[
            RegexValidator(
                r'^\d{5}-\d{3}$',
                'Formato de CEP inválido. Use: XXXXX-XXX.'
            )
        ]
    )
    logradouro = models.CharField(max_length=100, verbose_name="Logradouro")
    numero = models.CharField(max_length=10, verbose_name="Número")
    bairro = models.CharField(max_length=50, verbose_name="Bairro")
    cidade = models.CharField(max_length=50, verbose_name="Cidade")
    estado = models.CharField(
        max_length=2,
        verbose_name="Estado (UF)",
        validators=[
            RegexValidator(
                r'^[A-Z]{2}$',
                'Use a sigla do estado com 2 letras maiúsculas (ex.: SP).'
            )
        ]
    )

    # Campos OPCIONAIS
    complemento = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Complemento"
    )
    referencia = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Ponto de Referência"
    )

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado}"

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"