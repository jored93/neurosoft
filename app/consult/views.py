from .serializers import GraphEcgSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from bson.objectid import ObjectId

class GraphEcgViewSet(viewsets.ModelViewSet):
    serializer_class = GraphEcgSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(_id=ObjectId(pk)).first()
    
    def list(self, request):
        graphEcgSerializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(graphEcgSerializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        if self.get_queryset(pk):
            graphEcgSerializer = self.serializer_class(self.get_queryset(pk))
            return Response(graphEcgSerializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)