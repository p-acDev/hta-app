from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Mesure
from .serializers import MesureSerializer

# Create your views here.

class MesureAPIView(APIView):

    def get(self, *args, **kwargs):
        mesures = Mesure.objects.all()
        #TODO: add load to google drive process
        serializer = MesureSerializer(mesures, many=True)
        return Response(serializer.data)