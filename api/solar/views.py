from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

import joblib

from solar.models import Solar
from solar.serializers import SolarSerializer

# Create your views here.
class CreateView(CreateAPIView):
    queryset = Solar.objects.all()
    serializer_class = SolarSerializer
    
    def create(self, request, *args, **kwargs):
        # Validar e salvar os dados recebidos
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()  # Salva o novo registro no banco
        
        # Carrega o modelo de predição
        model_path = 'solar/regressao/model.pkl'
        model = joblib.load(model_path)
        investimento = instance.valor_placa * instance.numero_placas
        previsao = model.predict([[0, instance.numero_placas, investimento, instance.valor_placa]])[0]
        print(previsao)

        # Retorna os resultados
        producao_total = previsao * 12 * 25
        valor_economizado = producao_total * instance.valor_energia - investimento
        return Response({'producao_media': previsao, 'producao_total': producao_total, 'economia': valor_economizado }, status=status.HTTP_201_CREATED)