from rest_framework import serializers

from solar.models import Solar

class SolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solar
        fields = [
            "numero_placas",
            "valor_placa",
            "valor_energia"
        ]