from django.db.models import Q
from rest_framework import viewsets, filters
from data.models import Data
from .serializers import DataSerializer


class DataView(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'name', 'description']

    def get_item_queryset(query=None):
        queryset = []
        queries = query.split(" ")  # python install 2019 = [python, install, 2019]
        for q in queries:
            items = Data.objects.filter(
                Q(title__icontains=q) |
                Q(name__icontains=q) |
                Q(description__icontains=q)
            ).distinct()

            for item in items:
                queryset.append(item)
        return list(set(queryset))
