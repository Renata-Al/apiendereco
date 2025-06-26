from rest_framework import serializers
from .models import Endereco

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'
        extra_kwargs = {
            'cep': {'required': True},
            'logradouro': {'required': True},
            'numero': {'required': True},
            'bairro': {'required': True},
            'cidade': {'required': True},
            'estado': {'required': True},
        }