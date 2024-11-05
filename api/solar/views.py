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
        previsao = model.predict([[6,0, instance.numero_placas, instance.temperatura, False, True, False, False ]])[0]
        print(previsao)


        # Calculos
        producao_total = 0
        temp_factor = abs(25 - instance.temperatura) / 2 * 0.01
        
        for i in range(301):
            degradation = 0.008/12 * i
            producao_total += previsao - (previsao * temp_factor) - (previsao * degradation)
        
        valor_economizado = producao_total * instance.valor_energia - investimento
        # Retorna os resultados
        return Response({'producao_media': previsao, 'producao_total': producao_total, 'economia': valor_economizado }, status=status.HTTP_201_CREATED)