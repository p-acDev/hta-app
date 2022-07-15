from rest_framework.response import Response
from rest_framework.decorators import api_view
from mesure.models import Mesure
from .serializer import MesureSerializer


@api_view(['GET'])
def get_data(request):
    mesures = Mesure.objects.all()
    serializer = MesureSerializer(mesures, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_mesure(request):
    serializer = MesureSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)