from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

import joblib
import pandas as pd

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
        investimento = (instance.valor_placa * instance.numero_placas) * 1.8
        
        
        client_data = pd.DataFrame()
        producao_total = 0
            
        for lifetime in range(301):
            client_data['Lifetime (Months)'] = [lifetime]
            client_data['Number of Plates'] = instance.numero_placas
            client_data['Average Temperature (C)'] = instance.temperatura
            predicted_production = model.predict(client_data)
            producao_total += predicted_production[0]
        
        valor_economizado = producao_total * instance.valor_energia - investimento
        # Retorna os resultados
        return Response({'producao_media': producao_total/300, 'producao_total': producao_total, 'economia': valor_economizado }, status=status.HTTP_201_CREATED)