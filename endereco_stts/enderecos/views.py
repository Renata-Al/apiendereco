from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Endereco
from .serializers import EnderecoSerializer

class EnderecoAPIView(APIView):
    # LISTAR TODOS OS ENDEREÇOS (GET)
    def get(self, request):
        enderecos = Endereco.objects.all()
        serializer = EnderecoSerializer(enderecos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # CRIAR UM NOVO ENDEREÇO (POST)
    def post(self, request):
        serializer = EnderecoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EnderecoDetalheAPIView(APIView):
    # BUSCAR UM ENDEREÇO ESPECÍFICO (GET)
    def get(self, request, pk):
        try:
            endereco = Endereco.objects.get(id=pk)
            serializer = EnderecoSerializer(endereco)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Endereco.DoesNotExist:
            return Response(
                {"erro": "Endereço não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

    # ATUALIZAR ENDEREÇO (PUT)
    def put(self, request, pk):
        try:
            endereco = Endereco.objects.get(id=pk)
            serializer = EnderecoSerializer(endereco, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Endereco.DoesNotExist:
            return Response(
                {"erro": "Endereço não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

    # DELETAR ENDEREÇO (DELETE)
    def delete(self, request, pk):
        try:
            endereco = Endereco.objects.get(id=pk)
            endereco.delete()
            return Response(
                {"mensagem": "Endereço excluído com sucesso"},
                status=status.HTTP_204_NO_CONTENT
            )
        except Endereco.DoesNotExist:
            return Response(
                {"erro": "Endereço não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )