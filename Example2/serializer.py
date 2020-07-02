from rest_framework import routers, viewsets, serializers
from Example2.models import Example2

class Example2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Example2
        fields = ('__all__')