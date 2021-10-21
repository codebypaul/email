from rest_framework import serializers
from .models import Supplier,Missing

class MissingSerializer(serializers.Serializer):
    class Meta:
        model=Missing
        fields='__all__'

class SupplierSerializer(serializers.Serializer):
    class Meta:
        model=Supplier
        fields='__all__'