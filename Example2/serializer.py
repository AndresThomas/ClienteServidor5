
from django.contrib.auth.models import User
from rest_framework import routers, viewsets, serializers
from rest_framework import serializers
from Example2.models import Example2
class Example2Serializers(serializers.ModelSerializer):    

    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    edad    = serializers.IntegerField()
    direccion = serializers.CharField()
    curp = serializers.CharField()
    
    def create(self,validate_data):
        instance = Example2()
        instance.name = validate_data.get('name')
        instance.edad = validate_data.get('edad')
        instance.direccion = validate_data.get('direccion')
        instance.curp = validate_data.get('curp')
        if instance.edad > 0 and instance.edad < 99:
            if len(instance.curp) == 16:
                instance.save()
                return instance
            else:
                raise serializers.ValidationError('Ingrese una curp validad')    
        else:
            raise serializers.ValidationError('Ingrese una edad validad')

    class Meta:
        model = Example2
        fields = ('__all__')

        