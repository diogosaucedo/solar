from rest_framework.generics import CreateAPIView

from solar.models import Solar
from solar.serializers import SolarSerializer

# Create your views here.
class CreateView(CreateAPIView):
    queryset = Solar.objects.all()
    serializer_class = SolarSerializer
    
