from rest_framework.serializers import ModelSerializer
from .models import Mesure

class MesureSerializer(ModelSerializer):

    class Meta:
        model = Mesure
        fields = '__all__'
