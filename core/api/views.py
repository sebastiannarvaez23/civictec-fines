from rest_framework import viewsets
from .serializers import CitationSerializer
from ..models import Citation

class CitationViewSet(viewsets.ModelViewSet):
    queryset = Citation.objects.all()
    serializer_class = CitationSerializer