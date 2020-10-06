from rest_framework import serializers
from rest_framework import Emp

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        #fields = {''}          #for specific field to be returned
        fields = '__all__'      #for all firlds to be returned
