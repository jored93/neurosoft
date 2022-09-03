from rest_framework import serializers
from .models import GraphEcg
from core.settings import BASE_DIR

base = str(BASE_DIR)

class GraphEcgSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraphEcg
        fields = '__all__'

    def to_representation(self, instance):
        return {
            '_id': str(instance._id),
            'filename': base + '/ECG_graficas/' + instance.filename,
            'url': instance.url,
        }